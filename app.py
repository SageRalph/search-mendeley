from flask import Flask, redirect, render_template, request, session
import yaml

from mendeley import Mendeley
from mendeley.session import MendeleySession


with open('config.yml') as f:
    config = yaml.load(f)

REDIRECT_URI = 'http://localhost:5000/oauth'

app = Flask(__name__)
app.debug = True
app.secret_key = config['clientSecret']

mendeley = Mendeley(config['clientId'], config['clientSecret'], REDIRECT_URI)


@app.route('/')
def login():
    # TODO Check for token expiry
    # if 'token' in session:
    #    return redirect('/library')

    auth = mendeley.start_authorization_code_flow()
    session['state'] = auth.state

    return redirect(auth.get_login_url())


@app.route('/oauth')
def auth_return():
    auth = mendeley.start_authorization_code_flow(state=session['state'])
    mendeley_session = auth.authenticate(request.url)

    session.clear()
    session['token'] = mendeley_session.token

    return redirect('/library')


@app.route('/library')
def list_documents():
    if 'token' not in session:
        return redirect('/')

    query = request.args.get('query')

    mendeley_session = get_session_from_cookies()

    name = mendeley_session.profiles.me.display_name

    if query:
        page = mendeley_session.documents.search(query, view='client').list()
    else:
        page = mendeley_session.documents.list(view='client')
        query = ''

    # De-paginate
    docs = []
    while hasattr(page, 'next_page'):
        docs += page.items
        page = page.next_page

    return render_template('library.html', name=name, docs=docs, query=query)


@app.route('/document')
def get_document():
    if 'token' not in session:
        return redirect('/')

    mendeley_session = get_session_from_cookies()

    document_id = request.args.get('document_id')
    doc = mendeley_session.documents.get(document_id)

    return render_template('details.html', doc=doc)


@app.route('/detailsLookup')
def details_lookup():
    if 'token' not in session:
        return redirect('/')

    mendeley_session = get_session_from_cookies()

    doi = request.args.get('doi')
    doc = mendeley_session.catalog.by_identifier(doi=doi)

    return render_template('details.html', doc=doc)


@app.route('/download')
def download():
    if 'token' not in session:
        return redirect('/')

    mendeley_session = get_session_from_cookies()

    document_id = request.args.get('document_id')
    doc = mendeley_session.documents.get(document_id)
    doc_file = doc.files.list().items[0]

    return redirect(doc_file.download_url)


@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect('/')


def get_session_from_cookies():
    return MendeleySession(mendeley, session['token'])


if __name__ == '__main__':
    app.run()

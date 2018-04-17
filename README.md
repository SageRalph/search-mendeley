# Search Mendeley

## How to run ##

1. Install [Python 2.7](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/).
2. Register your client at the [developer portal](http://dev.mendeley.com). Use `http://localhost:5000/oauth` as your  Redirect URI. This will give you a client ID and secret.
3. Rename the config.yml.example file to config.yml, and fill in your client ID and secret in this file.
4. Run the following command to install dependencies:

        pip install -r requirements.txt

5. Start the server:

		app.py

6. Go to http://localhost:5000 in your browser.

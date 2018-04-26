# Search Mendeley
Search Mendeley provides advanced tools for browsing and searching your Mendeley library, including annotation search.

## Setup ##

1. Install [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/).

2. Install pipenv

        $ pip install pipenv

3. [Register your client](https://dev.mendeley.com/reference/topics/application_registration.html).  
If running locally, use `http://localhost:5000/oauth` as your  Redirect URI.  
This will give you a client ID and secret.

4. Navigate to the /app directory

5. Rename the config.yml.example file to config.yml, and fill in your client ID and secret in this file.

6. Install dependencies using pipenv

        $ pipenv install

## How to run ##

On Windows, launch the application by running RUN.bat

Otherwise, naviagte to the /app directory and run app.py using pipenv  
Then go to http://localhost:5000 in your browser.

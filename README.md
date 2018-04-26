# Search Mendeley
Search Mendeley provides advanced tools for browsing and searching your Mendeley library, including annotation search.

## Setup ##

1. Install [Python 2.7](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/).

2. [Register your client](https://dev.mendeley.com/reference/topics/application_registration.html).  
If running locally, use `http://localhost:5000/oauth` as your  Redirect URI.  
This will give you a client ID and secret.

3. Navigate to the /app directory

4. Rename the config.yml.example file to config.yml, and fill in your client ID and secret in this file.

5. Run the following command to install dependencies:

        pip install -r requirements.txt

## How to run ##

On Windows, launch the application by running RUN.bat

Otherwise, naviagte to the /app directory and run app.py using Python 2.7  
Then go to http://localhost:5000 in your browser.

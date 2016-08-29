# WizWeek Python API

This is a simple Python Flask API for the weekly schedule optimizer website,
[wizweek.com](https://wizweek.com).

It handles authentication by taking a user's Google account bearer token in the
`Authorization` header. It will then verify that token against the Google API.

Currently the only endpoint that is supported is the `/settings` endpoint which
supports `GET` and `PUT` to retrieve and save the user's settings respectively.

## Authentication

Authentication works by sending a `Bearer [Google token]` value in the
`Authorization` header.

## Supported endpoints

`PUT /settings`: saves new settings for a user
`GET /settings`: retrieves settings for a user or {} if user has no settings yet

`GET /tasks`: retrieves the list of tasks for the user
`POST /tasks`: creates a new task and returns its `id`
`PUT /task/:id`: updates a task's data
`DELETE /task/:id`: deletes a task

## How to reset the dependencies

Here's how to refresh/update the dependencies (make sure you are using Python
    3.5):
```
virtualenv --clear venv
pip install -r base-requirements.txt && pip freeze > requirements.txt
```

## Deploying to Heroku 

Currently this is set up to be easily deployed to heroku via `git push heroku
master`. It isn't configured to auto-deploy at this time.

## Setting environment variables

For app secrets and some config for this API, set its environment variables.

The trickiest is the authorization key variable which must be in base64.
To format the json Google Cloud API credentials file for easy use in an 
environment variable we will encode it to base64 like this: 
`cat YourProject-abcd1234.json | base64`. Then you can copy and paste that from 
the terminal into your environment variable `SERVICE_ACCOUNT_JSON_BASE64`.

You also need a random secret key for the Flask app for the `FLASK_SECRET_KEY`.
Some string of random data will do just fine
(e.g. generated via `openssl rand -base64 32`).

## License and Acknowledgements

The Google token processing is adapted from a Flask example snippet at 
http://flask.pocoo.org/snippets/125/ .

Other code is Copyright David Raffensperger and MIT licensed.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

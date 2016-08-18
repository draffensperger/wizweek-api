# WizWeek API

This is a simple Python Flask API for the weekly schedule optimizer website,
[wizweek.com](https://wizweek.com).

It handles authentication by taking a user's Google account bearer token in the
`Authorization` header. It will then verify that token against the Google API.

Currently the only endpoint that is supported is the `/settings` endpoint which
supports `GET` and `PUT` to retrieve and save the user's settings respectively.

## Developing locally

To refresh the dependencies
source venv/bin/activate

```
virtualenv --clear venv
pip install -r base-requirements.txt && pip freeze > requirements.txt
```
pip install -r requirements.txt

## Prerequisites



## Deploying to Heroku

Create a Google Cloud Platform project and authorize it to use the Google
Cloud Datastore service. Then download a .json credentials file.

For simplicity of deployment, we will be setting the credentials via an
environment variable.

To format the json for easy use in an environment variable we will encode it to
base64 like this: 
`cat YourProject-abcd1234.json | base64`

Then you can copy and paste that from the terminal into your environment
variable. If you're on a Mac, you could also do `cat YourProject-abcd1234.json | base64 | pbcopy` to pipe it to the clipboard directly.

You also need a random secret key for the Flask app. Some string of random
data will do just fine (e.g. generated via `openssl rand -base64 32`).

## Deploying the AngularJS front-end



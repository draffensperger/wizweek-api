# WizWeek

Source code for a weekly planning application. This handles authenticating
users with Google login, and an interface for settings and tasks.

Currently it integrates with Google tasks, so you can see your WizWeek tasks there as
well.

This is an AngularJS application (and a bit of Python + Flask).

It makes use of the [scheduler] web service to do the actual schedule
optimization.

## Deploying the Flask (Python) backend

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



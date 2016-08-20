import os
import datetime
import json
from gcloud import datastore
from flask import *
from flask_restful import *
from google_authorized_decorator import google_authorized
from datastore_setup import datastore_client_from_env
from flask_sslify import SSLify
from flask_cors import CORS

app = Flask(__name__)
api = Api(app) 
SSLify(app)
CORS(app, origins=os.environ['CORS_ORIGINS'].split(','))
db = datastore_client_from_env()

class Settings(Resource):
    @google_authorized
    def get(self, user_email):
        user = db.get(db.key('User', user_email))
        if user is None:
            # If the user has no settings, return an empty object. The client
            # will fill it in with appropriate default values.
            return jsonify({})
        return jsonify(json.loads(user['settings']))

    @google_authorized
    def put(self, user_email):
        if not request.json:
            abort(400)
        key = db.key('User', user_email)
        user = datastore.Entity(key, exclude_from_indexes=['settings'])
        user['updated'] = datetime.datetime.utcnow()
        user['settings'] = json.dumps(request.json)
        db.put(user)
        return jsonify({ 'success': True })

api.add_resource(Settings, '/settings')

# Allow a simple root URL for pinging the service.
@app.route('/')
def root():
    return 'OK'

if __name__ == '__main__':
    app.secret_key = str(os.environ['FLASK_SECRET_KEY'])
    app.debug = os.environ['FLASK_DEBUG'].lower() == 'true'
    app.run()

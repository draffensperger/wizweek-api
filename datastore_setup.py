import os
import json
import base64
from oauth2client import service_account
from gcloud import datastore

def datastore_client_from_env():
    creds_json = base64.b64decode(os.environ['SERVICE_ACCOUNT_JSON_BASE64']).decode()
    creds_dict = json.loads(creds_json)
    cred = service_account.ServiceAccountCredentials.from_json_keyfile_dict(creds_dict)
    return datastore.Client(project=creds_dict['project_id'], credentials=cred)

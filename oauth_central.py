import requests
import json

# Let our global vars
token = ""
partnerid = ""
apihost = ""


def authenticate(client_id, client_secret):
    global token  # Set global for access for other functions
    uri = "https://id.sophos.com/api/v2/oauth2/token"

    d = {'grant_type': 'client_credentials',
         'client_id': client_id,
         'client_secret': client_secret,
         'scope': 'token'
         }
    r = requests.post(uri, data=d)

    if r.status_code == 200:
        j = json.loads(r.text)
        token = j['access_token']
        whoami(token)
        return True

    else:
        print("Authentication failed")
        return False


def whoami(token):
    global partnerid
    global apihost

    uri = 'https://api.central.sophos.com/whoami/v1'

    h = {'Authorization': f'Bearer {token}'}
    r = requests.get(uri, headers=h)
    if r.status_code == 200:
        j = json.loads(r.text)
        partnerid = j['id']
        apihost = j['apiHosts']['global']
        return True
    else:
        print("Unable to obtain whoami Details")
        return False

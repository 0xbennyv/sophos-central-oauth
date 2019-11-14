import requests
import json
import oauth_central as central  # Import the oauth module


def list_tenants():
    client_id = ""
    client_secret = ""
    central.authenticate(client_id, client_secret)
    uri = 'https://api.central.sophos.com/partner/v1/tenants?pageTotal=true'

    h = {'Authorization': f'Bearer {central.token}',
         'X-Partner-ID': central.partnerid}
    r = requests.get(uri, headers=h)

    if r.status_code == 200:
        j = json.loads(r.text)
        print(j)
        return True
    else:
        print("Unable to get tenant lists")
        return False


list_tenants()

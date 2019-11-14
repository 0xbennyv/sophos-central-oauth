# Getting Started

Quick implimentation of oauth2 with the SOPHOS API Gateway documented at https://developer.sophos.com. Import the module, then you can pass the authenticate function a client_id and client_secret which will can then be used in other functions by calling central.token, central.partnerid and central.apihost.

```
import oauth_central as central
central.authenticate(client_id, client_secret)
h = {'Authorization': f'Bearer {central.token}', 'X-Partner-ID': central.partnerid}
```

from requests.sessions import session, Session
from requests.auth import HTTPBasicAuth
from . import api

class UmbrellaClient():
    s: Session = session()

    destination_lists   : api.DestinationListAPI
    deployments         : api.DeploymentsAPI

    def _get_token(self):
        res = self.s.post(
            'https://api.umbrella.com/auth/v2/token',
            data={
                'grant_type':'client_credentials'
            }
        )
        res.raise_for_status()
        return res.json()['access_token']

    def __init__(self, api_key: str, api_secret: str):
        self.s.auth = HTTPBasicAuth(api_key, api_secret)

        token = self._get_token()
        self.s.auth = None
        self.s.headers['Authorization'] = f'Bearer {token}'

        # Map APIs
        self.destination_lists  = api.DestinationListAPI(self)
        self.deployments        = api.DeploymentsAPI(self)

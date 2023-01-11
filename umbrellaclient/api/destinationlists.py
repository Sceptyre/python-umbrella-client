from .base import _BaseAPI

class DestinationListAPI(_BaseAPI):
    # Destination List interactions
    def get_destination_list(self, destination_list_id: str):
        res = self._uc.s.get(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id
        )
        res.raise_for_status()

        return res.json()
    
    def get_destination_lists(self):
        res = self._uc.s.get(
            'https://api.umbrella.com/policies/v2/destinationlists'
        )
        res.raise_for_status()

        return res.json()


    # Destination interactions
    def add_destination_list_destination(self, destination_list_id: str, destination: str, type: str='DOMAIN', comment: str='Added By Automation'):
        res = self._uc.s.post(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id + '/destinations',
            json=[
                {
                    'destination': destination,
                    'comment': comment
                }
            ]
        )
        res.raise_for_status()

        return res.json()

    def get_destination_list_destinations(self, destination_list_id: str, page: int=1, limit: int=100):
        res = self._uc.s.get(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id + '/destinations',
            params={
                'page':page,
                'limit':limit
            }
        )
        res.raise_for_status()

        return res.json()

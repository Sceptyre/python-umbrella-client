from ..base import _BaseAPI

class RoamingComputersAPI(_BaseAPI):
    __base_url__ = 'https://api.umbrella.com/deployments/v2/roamingcomputers'

    def get_roaming_computer(self, roaming_computer_id: str):
        res = self._uc.s.get(
            f"{self.__base_url__}/{roaming_computer_id}"
        )
        res.raise_for_status()

        return res.json()

    def get_roaming_computers(self):
        res = self._uc.s.get(
            self.__base_url__
        )
        res.raise_for_status()

        return res.json()
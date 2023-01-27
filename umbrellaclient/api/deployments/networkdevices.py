from ..base import _BaseAPI

from ...models import network_device as network_device_models

class NetworkDevicesAPI(_BaseAPI):
    __base_url__ = 'https://api.umbrella.com/deployments/v2/networkdevices'

    def get_network_device(self, network_device_id: str):
        res = self._uc.s.get(
            f"{self.__base_url__}/{network_device_id}"
        )
        res.raise_for_status()

        return res.json()

    def get_network_devices(self):
        res = self._uc.s.get(
            self.__base_url__
        )
        res.raise_for_status()

        return res.json()

    def update_network_device(self, network_device_id: str, **kwargs):
        body = network_device_models.UpdateNetworkDeviceRequest( **kwargs )

        res = self._uc.s.patch(
            f"{self.__base_url__}/{network_device_id}",
            json=body
        )
        res.raise_for_status()

        return res.json()
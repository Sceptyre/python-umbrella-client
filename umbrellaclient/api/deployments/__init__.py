from ..base import _BaseAPI

from .networkdevices    import NetworkDevicesAPI
from .roamingcomputers  import RoamingComputersAPI

class DeploymentsAPI(_BaseAPI):
    networkdevices  : NetworkDevicesAPI
    roamingcomputers: RoamingComputersAPI

    def __post_init__(self):        
        self.networkdevices     = NetworkDevicesAPI(self._uc)
        self.roamingcomputers   = RoamingComputersAPI(self._uc)
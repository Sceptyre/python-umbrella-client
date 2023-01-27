class _BaseAPI():
    __base_url__: str

    def __post_init__(self): pass

    def __init__(self, umbrella_client):
        self._uc = umbrella_client

        self.__post_init__()
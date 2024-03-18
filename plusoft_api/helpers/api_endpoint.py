from plusoft_api.helpers.base_requests import BaseRequests, BasicAuth


class BaseApiEndpoint:
    def __init__(
        self,
        basic_auth: BasicAuth,
        domain: str,
        endpoint_path: str = "/",
    ) -> None:
        self._basic_auth = basic_auth
        self.base_requests: BaseRequests = BaseRequests(
            domain=domain, basic_auth=basic_auth, endpoint_path=endpoint_path
        )
        self.domain = domain


class ImportEndpoint(BaseApiEndpoint):
    def __init__(
        self, basic_auth: BasicAuth, domain: str, endpoint_path: str = ""
    ) -> None:
        super().__init__(basic_auth, domain, f"/import{endpoint_path}")


class ConsultEndpoint(ImportEndpoint):
    def __init__(
        self, basic_auth: BasicAuth, domain: str, endpoint_path: str = ""
    ) -> None:
        super().__init__(basic_auth, domain, f"/consult{endpoint_path}")

from plusoft_api.helpers.base_requests import BaseRequests


class ApiEndpoint:
    def __init__(
        self,
        username: str,
        password: str,
        domain: str,
        endpoint_path: str = "/",
    ) -> None:
        self.base_requests: BaseRequests = BaseRequests(
            username=username, password=password, domain=domain
        )
        self.endpoint_path: str = endpoint_path

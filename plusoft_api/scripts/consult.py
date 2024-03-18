from plusoft_api.helpers.api_endpoint import BasicAuth, ConsultEndpoint
from plusoft_api.models.consult import RequisitionStatus


class Consult(ConsultEndpoint):
    def __init__(self, basic_auth: BasicAuth, domain: str) -> None:
        super().__init__(domain=domain, basic_auth=basic_auth)

    def consult_status(self, consult_code: int) -> dict:
        payload = {"code": consult_code}

        return self.base_requests.post(path="", json=payload)


class RequisitionProccess:
    def __init__(
        self,
        basic_auth: BasicAuth,
        domain: str,
        message: str,
        consult_code: int = None,
        error: bool = None,
    ) -> None:
        if error:
            raise ValueError(message)

        self.message: str = message
        self.consult_code: int = consult_code
        self.consult_client: Consult = Consult(basic_auth=basic_auth, domain=domain)

    @property
    def requisition_status(self) -> RequisitionStatus:
        return RequisitionStatus(
            **self.consult_client.consult_status(self.consult_code)
        )

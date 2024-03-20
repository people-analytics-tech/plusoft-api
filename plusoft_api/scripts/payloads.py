from typing import Literal, Union

from plusoft_api.helpers.api_endpoint import BaseApiEndpoint
from plusoft_api.models.aux import PayloadDataClass
from plusoft_api.scripts.consult import RequisitionProccess
from plusoft_api.utils.aux_functions import clean_none_values_dict


class BasePayload:
    def __init__(
        self, payload_factory: PayloadDataClass, endpoint: BaseApiEndpoint
    ) -> None:
        self.endpoint = endpoint
        self.payload_factory = payload_factory
        self.staged_payload: list[PayloadDataClass] = []

    def payload(
        self, load_type: Literal["full", "without_none_fields"] = "without_none_fields"
    ) -> list[dict]:
        if load_type == "without_none_fields":
            return [
                clean_none_values_dict(dict(item.as_dict))
                for item in self.staged_payload
            ]

        else:
            return [dict(item.as_dict) for item in self.staged_payload]

    def add_to_payload(self, **kwargs):
        self.staged_payload.append(self.payload_factory(**kwargs))

    def upload(
        self,
        path: str,
        load_type: Literal["full", "without_none_fields"] = "without_none_fields",
    ) -> Union[RequisitionProccess, None]:
        if not self.staged_payload:
            print(
                "Request not sent because you no have items added to staged payload. You need to add some items with add_to_payload method before try upload."
            )
            return None

        return RequisitionProccess(
            basic_auth=self.endpoint._basic_auth,
            domain=self.endpoint.domain,
            **self.endpoint.base_requests.post(path=path, json=self.payload(load_type)),
        )


class BaseImportsPayload:
    def __init__(
        self, endpoint: BaseApiEndpoint, path: str, payload_factory: PayloadDataClass
    ) -> None:
        self.path = path
        self._payload: BasePayload = BasePayload(
            payload_factory=payload_factory, endpoint=endpoint
        )
        self.__keys: list[str] = []

    def add_to_payload(self, primary_key: str = None, **kwargs):
        """Override in subclass"""
        if primary_key:
            if kwargs[primary_key] not in self.__keys:
                self._payload.add_to_payload(**kwargs)
                self.__keys.append(kwargs[primary_key])

            else:
                raise ValueError(
                    f"Record not added to payload because {primary_key} {kwargs[primary_key]} already exist into staged payload."
                )

        else:
            self._payload.add_to_payload(**kwargs)

    def upload(
        self, load_type: Literal["full", "without_none_fields"] = "without_none_fields"
    ) -> Union[RequisitionProccess, None]:
        requisition = self._payload.upload(path=self.path, load_type=load_type)
        self.clear_staged_payload()
        return requisition

    def clear_staged_payload(self) -> None:
        self._payload.staged_payload = []

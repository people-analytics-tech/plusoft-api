from dataclasses import asdict, dataclass
from typing import Literal

from plusoft_api.models.aux import NestedDataClass


@dataclass
class Error:
    tx_error: str
    tx_errorline: str
    nr_errorline: int
    tx_cause: str


@dataclass
class Logs(NestedDataClass):
    success: int
    total: int
    errors: list[Error]


@dataclass
class RequisitionStatus(NestedDataClass):
    status: Literal["P", "R", "S"]
    message: str
    logs: Logs = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)

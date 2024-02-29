# This module contains aux types used in api


from enum import Enum
from typing import Literal

YesNo = Literal["sim", "nao"]


class GroupsOptions(int, Enum):
    ADD_GROUPS = 1
    FULL_UPDATE = 2
    REMOVE_GROUPS = 3
    REMOVE_ALL_GROUPS = 4

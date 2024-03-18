# This module contains aux types used in api


from enum import Enum


class GroupsOptions(int, Enum):
    ADD_GROUPS = 1
    FULL_UPDATE = 2
    REMOVE_GROUPS = 3
    REMOVE_ALL_GROUPS = 4


class YesNoEnum(int, Enum):
    yes = 1
    no = 0

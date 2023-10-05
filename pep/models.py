import json
from enum import Enum
from typing import List


class Clearance(Enum):
    PUBLIC = 0
    BRONZE = 1
    SILVER = 2
    GOLD = 3


class Document(object):
    def __init__(self, name: str, clearance: Clearance, attributes: List[str] = None):
        self._name = name
        self._clearance = clearance
        self._attributes = attributes or []

    @property
    def name(self) -> str:
        return self._name

    @property
    def clearance(self) -> Clearance:
        return self._clearance

    @property
    def attributes(self) -> List[str]:
        return self._attributes

    def to_dict(self):
        return {
            "name": self.name,
            "clearance": self.clearance.value,
            "attributes": self.attributes,
        }


class User(object):
    def __init__(self, name: str, clearance: Clearance, attributes: List[str] = None):
        self._name = name
        self._clearance = clearance
        self._attributes = attributes or []

    @property
    def name(self) -> str:
        return self._name

    @property
    def clearance(self) -> Clearance:
        return self._clearance

    @property
    def attributes(self) -> List[str]:
        return self._attributes

    def to_dict(self):
        return {
            "name": self.name,
            "clearance": self.clearance.value,
            "attributes": self.attributes,
        }

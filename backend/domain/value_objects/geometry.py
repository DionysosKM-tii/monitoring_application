from typing import Protocol

class Geometry(Protocol):
    def to_dict(self) -> dict: ...
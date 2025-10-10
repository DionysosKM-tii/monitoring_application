from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Entity:
    id: int = field(init=False, default=None)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

from dataclasses import dataclass

@dataclass(frozen=True)
class AreaDetailsDTO:
    area_id: int
    area_name: str

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class VersionResponse:
    region: str
    set_name: str
    started_at: datetime
    set: int
    version: List[str]

    def __init__(
        self,
        region="",
        set_name="",
        started_at=datetime.today(),
        set=0,
        version=[],
    ) -> None:
        self.region = region
        self.set_name = set_name
        self.started_at = started_at
        self.set = set
        self.version = version

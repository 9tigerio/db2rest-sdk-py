from dataclasses import dataclass
from typing import Dict, List, Any, Optional

@dataclass
class CreateResponse:
    row: int
    keys: Dict[str, Any]

@dataclass
class CreateBulkResponse:
    rows: List[int]
    keys: Dict[str, Any]

@dataclass
class UpdateResponse:
    rows: int

@dataclass
class DeleteResponse:
    rows: int

@dataclass
class CountResponse:
    count: int

@dataclass
class ExistsResponse:
    exists: bool

@dataclass
class JoinDetail:
    table: str
    with_table: str
    fields: List[str]
    on: List[str]
    schema_name: Optional[str] = None
    filter: Optional[str] = None
    join_type: Optional[str] = None

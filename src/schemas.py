from dataclasses import dataclass, asdict, field
from typing import List

@dataclass
class Entity:
    text: str
    label: str
    start: int
    end: int
    confidence: float

@dataclass
class Clause:
    clause_id: int
    text: str
    page: int
    word_count: int
    entities: List[Entity] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

@dataclass
class ContractAnalysis:
    status: str
    total_clauses: int
    clauses: List[Clause]

    def to_dict(self):
        return asdict(self)

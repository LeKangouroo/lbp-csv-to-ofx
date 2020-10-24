from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Transaction:
    date: datetime
    memo: str
    amount_euros: str
    amount_francs: str

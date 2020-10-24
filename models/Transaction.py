from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    date: datetime
    memo: str
    amount: Decimal
    amount_francs: Decimal

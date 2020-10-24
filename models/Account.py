from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Account:
    number: str
    type: str
    currency: str
    balance_date: datetime
    balance: Decimal
    balance_francs: Decimal

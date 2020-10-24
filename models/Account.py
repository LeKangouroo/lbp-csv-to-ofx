from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    number: str
    type: str
    currency: str
    balance_date: str
    balance_euros: str
    balance_francs: str

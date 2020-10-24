from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    date: str
    memo: str
    amount_euros: str
    amount_francs: str

from dataclasses import dataclass
from models.Account import Account
from models.Transaction import Transaction
from typing import List


@dataclass(frozen=True)
class Data:
    account: Account
    transactions: List[Transaction]

from csv import reader

from models.Account import Account
from models.Data import Data
from models.Transaction import Transaction


def parse_csv(path):
    _transactions = []
    _offset = 8
    with open(path, newline="") as csv_file:
        _reader = reader(csv_file, delimiter=";", quotechar='"')
        for _row in _reader:
            _line = _reader.line_num
            if _line == 1:
                _account_number = _row[1]
            elif _line == 2:
                _account_type = _row[1]
            elif _line == 3:
                _account_currency = _row[1]
            elif _line == 4:
                _account_balance_date = _row[1]
            elif _line == 5:
                _account_balance_euros = _row[1]
            elif _line == 6:
                _account_balance_francs = _row[1]
            elif _line > _offset:
                _transactions.append(Transaction(date=_row[0], memo=_row[1], amount_euros=_row[2], amount_francs=_row[3]))
    _account = Account(
        number=_account_number,
        type=_account_type,
        currency=_account_currency,
        balance_date=_account_balance_date,
        balance_euros=_account_balance_euros,
        balance_francs=_account_balance_francs)
    _data = Data(account=_account, transactions=_transactions)
    return _data


def convert_csv_to_ofx(path):
    _data = parse_csv(path=path)
    print(_data.account)
    for t in _data.transactions:
        print(t)
    return "toto"

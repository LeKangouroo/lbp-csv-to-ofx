import uuid

from csv import reader
from datetime import datetime
from decimal import Decimal
from ofxtools.models import SONRS, STATUS, SIGNONMSGSRSV1, OFX, LEDGERBAL, BANKACCTFROM, STMTRS, STMTTRNRS, \
    BANKMSGSRSV1, BANKTRANLIST
from ofxtools.utils import UTC
from models.Account import Account
from models.Data import Data
from models.Transaction import Transaction
from pytz import timezone
from xml.etree import ElementTree


def get_ofx_account_type(account: Account):
    _mapping = {
        "CCP": "CHECKING"
    }
    return _mapping.get(account.type, _mapping["CCP"])


def get_ofx_account_currency(account: Account):
    _mapping = {
        "euros": "EUR"
    }
    return _mapping.get(account.currency, _mapping["euros"])


def parse_amount(amount: str):
    return Decimal(amount.replace(" ", "").replace(",", "."))


def parse_date(date_str: str, date_format: str = "%d/%m/%Y", tz: str = "Europe/Paris"):
    _date = datetime.strptime(date_str, date_format)
    _timezone = timezone(tz)
    return _timezone.localize(_date)


def parse_csv(path: str):
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
                _account_balance_date = parse_date(_row[1])
            elif _line == 5:
                _account_balance_euros = parse_amount(_row[1])
            elif _line == 6:
                _account_balance_francs = parse_amount(_row[1])
            elif _line > _offset:
                _transactions.append(
                    Transaction(
                        date=parse_date(_row[0]),
                        memo=_row[1],
                        amount_euros=parse_amount(_row[2]),
                        amount_francs=parse_amount(_row[3])))
    _account = Account(
        number=_account_number,
        type=_account_type,
        currency=_account_currency,
        balance_date=_account_balance_date,
        balance_euros=_account_balance_euros,
        balance_francs=_account_balance_francs)
    _data = Data(account=_account, transactions=_transactions)
    return _data


def convert_csv_to_ofx(path: str):
    _data = parse_csv(path=path)
    _ledger_balance = LEDGERBAL(
        balamt=_data.account.balance_euros,
        dtasof=_data.account.balance_date)
    _account_description = BANKACCTFROM(
        bankid="000",
        acctid=_data.account.number,
        accttype=get_ofx_account_type(_data.account))
    _bank_transactions = BANKTRANLIST(
        dtstart=_data.account.balance_date,
        dtend=_data.account.balance_date)
    _statement_res = STMTRS(
        curdef=get_ofx_account_currency(_data.account),
        bankacctfrom=_account_description,
        banktranlist=_bank_transactions,
        ledgerbal=_ledger_balance)
    _status = STATUS(code=0, severity="INFO")
    _statement_transaction_res = STMTTRNRS(trnuid=str(uuid.uuid4()), status=_status, stmtrs=_statement_res)
    _bank_msg_res = BANKMSGSRSV1(_statement_transaction_res)
    _sign_on_res = SONRS(status=_status, dtserver=datetime.now(tz=UTC), language="FRA")
    _sig_on_msg_res = SIGNONMSGSRSV1(sonrs=_sign_on_res)
    return OFX(signonmsgsrsv1=_sig_on_msg_res, bankmsgsrsv1=_bank_msg_res)


def serialize_ofx(ofx: OFX):
    _root = ofx.to_etree()
    return ElementTree.tostring(_root).decode()

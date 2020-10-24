import csv
import ofxtools.models


def parse_csv(path, fieldnames, offset):
    _output = []
    with open(path, newline="") as csv_file:
        _reader = csv.DictReader(csv_file, delimiter=";", quotechar='"', fieldnames=fieldnames)
        for _row in _reader:
            if _reader.line_num < offset:
                continue
            _output.append(_row)
    return _output


def convert_csv_to_ofx(path, fieldnames, offset):
    _csv = parse_csv(path=path, fieldnames=fieldnames, offset=offset)


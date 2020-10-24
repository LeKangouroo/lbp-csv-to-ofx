from functions import parse_csv
from sys import argv


if len(argv) < 2:
    print("No input file path given")
    exit(1)

csv_data = parse_csv(path=argv[1], fieldnames=['date', 'memo', 'amount_euros', 'amount_francs'], offset=9)
for row in csv_data:
    print(f'{row["date"]} | {row["memo"]} | {row["amount_euros"]}')

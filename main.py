from functions import convert_csv_to_ofx
from sys import argv


if len(argv) < 2:
    print("No input file path given")
    exit(1)

ofx = convert_csv_to_ofx(path=argv[1], fieldnames=['date', 'memo', 'amount_euros', 'amount_francs'], offset=9)
print(ofx)
# for row in csv_data:
#     print(f'{row["date"]} | {row["memo"]} | {row["amount_euros"]}')

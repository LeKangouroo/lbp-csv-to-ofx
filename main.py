from functions import convert_csv_to_ofx, serialize_ofx
from sys import argv


if len(argv) < 2:
    print("No input file path given")
    exit(1)

ofx = serialize_ofx(convert_csv_to_ofx(path=argv[1]))
print(ofx)
# for row in csv_data:
#     print(f'{row["date"]} | {row["memo"]} | {row["amount"]}')

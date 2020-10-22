import csv

from sys import argv

if len(argv) < 2:
    print("No input file path given")
    exit(1)

rows_offset = 9
input_file_path = argv[1]
fieldnames = ['date', 'memo', 'amount_euros', 'amount_francs']

with open(input_file_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";", quotechar='"', fieldnames=fieldnames)
    for row in reader:
        if reader.line_num < rows_offset: continue
        print(f'row {reader.line_num} -> {row["date"]} | {row["memo"]} | {row["amount_euros"]}')

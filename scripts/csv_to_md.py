import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, newline='') as f:
    reader = list(csv.reader(f))

headers = reader[0]
rows = reader[1:]

def format_row(row):
    return "| " + " | ".join(row) + " |"

with open(output_file, "w") as f:
    f.write(format_row(headers) + "\n")
    f.write("|" + "|".join(["---"] * len(headers)) + "|\n")
    
    for row in rows:
        f.write(format_row(row) + "\n")
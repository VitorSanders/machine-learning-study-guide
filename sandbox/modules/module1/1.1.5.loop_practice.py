import csv
import os

# construct a path relative to this script's directory
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'title.basics.csv')

print(f"Reading from: {file_path}")

with open(file_path, encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        try:
            year = int(row[3])
        except (ValueError, IndexError):
            continue
        if year > 2000: 
            print(row[1])
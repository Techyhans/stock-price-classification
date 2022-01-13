import time

from googletrans import Translator
import csv

file = open('data.csv', encoding='utf8')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

translator = Translator()

# dest
# open the file in the write mode
f = open('data_final.csv', 'w', encoding="utf-8")
# create the csv writer
writer = csv.writer(f)
dest_header = ["original", "translated", "date", "price_moment"]
writer.writerow(dest_header)

rows = []
dest_rows = []
for row in csvreader:

    try:
        rows.append(row)

        result = translator.translate(str(row[0]), dest='en')

        # print(result.src)
        # print(result.dest)
        # print(result.origin)
        # print(result.text)
        # print('-------------------')

        # dest_rows.append([result.origin, result.text, row[1], row[2]])

        writer.writerow([result.origin, result.text, row[1], row[2]])
        time.sleep(1)
    except:
        print('error', row)

# close the file
f.close()

import time

from googletrans import Translator
import csv

from textblob import TextBlob
from langdetect import detect

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
dest_header = ["original", "Headline", "date", "Price movement"]
writer.writerow(dest_header)

rows = []
dest_rows = []
for row in csvreader:

    try:

        # result = translator.translate(str(row[0]), dest='en')

        lang = detect(str(row[0]))
        print(lang)
        if lang == "en":
            print("in")
            writer.writerow([str(row[0]), str(row[0]), row[1], row[2]])
        time.sleep(1)
    except Exception as e:
        print('error', row, e)

# close the file
f.close()

import requests
import json
import csv

# custom search key
KEY =  "" #ENTER API KEY HERE
# custom search engine id
ENGINE = "" #ENTER CUSTOM SEARCH ENGINE ID HERE
# in file
FILEIN = "" #ENTER INPUT FILE NAME HERE
# out file
FILEOUT = "" #ENTER OUTPUT FILE NAME HERE
# number of rows to search
numToQuery = 2

out = {}
cnt = 0
# open and iterate over csv
with open(FILEIN) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        
        if cnt >= numToQuery:
            break
        out[cnt] = []

        # build query string
        query = row[0].replace(" ","+") + "+" + row[1] + "+" + row[2]

        # add to outbound csv
        out[cnt].append(row[0])
        out[cnt].append(row[1])
        out[cnt].append(row[2])

        # perform query
        print("Searching for... ",row[0])
        p = {
            'key': KEY,
            'cx': ENGINE,
            'q': query
        }
        r = requests.get("https://www.googleapis.com/customsearch/v1?",params=p)

        #deserialize
        data = json.loads(r.text)
        item = data['items'][0]

        print("\t",item['title'])
        print("\t",item['link'].replace("\n",""))

        # add search results to outbound csv
        out[cnt].append(item['title'])
        out[cnt].append(item['link'])

        cnt = cnt+1

# write out csv file
with open(FILEOUT, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    for rowNum in out:
        print(rowNum)
        row = out[rowNum]
        writer.writerow(row)
    
input()
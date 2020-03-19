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
numToQuery = 50

out = []
cnt = 0
# open and iterate over csv
# start standard
with open(FILEIN) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
    # end standard
        
        if cnt >= numToQuery:
            break
        out.append([])

        # build query string
        query = row[0].replace(" ","+") + "+" + row[1] + "+" + row[2]

        # perform query
        print("Searching for... ",row[0])
        p = {
            'key': KEY,
            'cx': ENGINE,
            'q': query
        }
        #standard
        r = requests.get("https://www.googleapis.com/customsearch/v1?",params=p)
        #end standard

        #deserialize
        #standard
        data = json.loads(r.text)
        #end standard
        item = data['items'][0]

        print("\t",item['title'])
        print("\t",item['link'])

        # add to outbound csv
        out[cnt].append(row[0])
        out[cnt].append(row[1])
        out[cnt].append(row[2])
        out[cnt].append(item['title'])
        out[cnt].append(item['link'])

        cnt = cnt+1

# write out csv file
# standard
with open(FILEOUT, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    # end standard
    for row in out:
        # standard
        writer.writerow(row)
        # end standard
    
input()
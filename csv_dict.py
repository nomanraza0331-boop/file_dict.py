import csv

with open ("employees.csv","r") as infile:
    csvReader=csv.DictReader(infile)
    for row in csvReader:
        print(list(row.values()))
        infile.close
       
'''
with open ("employees.csv","r") as infile:
    csvreader=csv.DictReader(infile)
    total=0
    for r in csvreader:
        if r["gender"]=="male":
            print(r["salary"])
            r["salary"]=str(int(r["salary"])+0.1*int(r["salary"]))
            print(r)
'''   
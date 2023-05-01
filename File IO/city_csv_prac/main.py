import csv

with open("countries.csv","r",newline="") as csvfile:
    csv_content=csv.reader(csvfile, delimiter=",",quotechar="\"")

    for row in csv_content:
        city=row[0]
        pop=row[1]

        print(f"{city} {pop}")


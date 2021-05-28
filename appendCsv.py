import csv
with open("data.csv","a",newline='') as csvfile:
    writer= csv.writer(csvfile)
    for x in range(9):
        writer.writerow(["Data 3", "Data 4"])
        
            
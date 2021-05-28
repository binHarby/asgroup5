import csv
with open("data.csv","w+",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Title","Desc"])
    writer.writerow(["Row 1","Some desc"])
    writer.writerow(["Row 2","Some desc"])
    writer.writerow(["Row 3","Some desc"])

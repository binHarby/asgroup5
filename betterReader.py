import csv
with open("world.csv","r",newline='',encoding="utf8") as csvfile:
    reader= csv.DictReader(csvfile)
    for row in reader:
        print(row['name'])
        
#{city,country, test center, vacent time,center_img,recoverd,infected}

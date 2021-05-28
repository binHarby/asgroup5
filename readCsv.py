import csv
with open("data.csv","r",newline='') as csvfile:
    reader= csv.reader(csvfile)
    for idx,row in enumerate(reader):
        
        for i in range(len(row)):
            print(row[i],end='|')
        print()
        if(idx==0):
            
            print("-------------------------------------")
   
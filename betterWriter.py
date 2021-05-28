#{city,country, test_center, free slots,center_img,recoverd,infected}
import csv
from random import seed
from random import randint
import time
seed(1)
citys=list()
countries=list()
geoid=list()
with open("world.csv","r",newline='',encoding="utf8") as csvfile:
    reader= csv.DictReader(csvfile)
    for row in reader:
            citys.append(str(row['name']))
            countries.append(str(row['country']))
            geoid.append(str(row['geonameid']))

with open("dataNew.csv","w+",newline='',encoding="utf8") as csvfile:
    fildnames=["City","Country","Country ID","Test Center","Free Slots","Center img","Recovered","Infected"]
    writer = csv.DictWriter(csvfile,fieldnames=fildnames)
    writer.writeheader()
    times=["Noon","Morning","Night"]
    for i in range(len(citys)):
        print(citys[i],end='|')
        if(i%10==1):
            print()
        for j in range(1,3):
            free=times[(-1)*(randint(0,3)):]
            if not free:
                 writer.writerow({"City":citys[i],"Country":countries[i],"Country ID":geoid[i],"Test Center":"Center"+str(j),"Free Slots":str("None"),"Center img":"https://post.psychcentral.com/wp-content/uploads/2020/08/covid_testing_center-1200x628-facebook-1200x628.jpg","Recovered":str(randint(10,50000)),"Infected":randint(50000,8090000)})
            else:
                for ftm in free:
                    writer.writerow({"City":citys[i],"Country":countries[i],"Country ID":geoid[i],"Test Center":"Center"+str(j),"Free Slots":str(ftm),"Center img":"https://post.psychcentral.com/wp-content/uploads/2020/08/covid_testing_center-1200x628-facebook-1200x628.jpg","Recovered":str(randint(10,50000)),"Infected":str(randint(50000,8090000))})
#,"Test Center":"Number 1","Free Slots":"None","Center img":"LINK","Recovered":"10","infected":"100000"




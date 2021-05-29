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
    fildnames=["City","Country","Country ID","Test Center","Free Slots","Center img","Recovered","Infected","Deaths","Vaccinations","News"]
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
                 writer.writerow({"City":citys[i],"Country":countries[i],"Country ID":geoid[i],"Test Center":"Center"+str(j),"Free Slots":str("None"),"Center img":"https://drive.google.com/file/d/1ArwjMghyjgEQVnoWtKAG_oHnuQRQE30H/view?usp=sharing"
                 ,"Recovered":str(randint(10,50000)),"Infected":str(randint(50000,8090000)),"Deaths":str(randint(50,8000)),"Vaccinations":str(randint(90000,8090000))
                 ,"News":"https://www.healthline.com/health-news/how-covid-19-surge-is-related-to-a-black-fungus-outbreak"})
            else:
                for ftm in free:
                    writer.writerow({"City":citys[i],"Country":countries[i],"Country ID":geoid[i],"Test Center":"Center"+str(j),"Free Slots":str(ftm),"Center img":"https://drive.google.com/file/d/1ArwjMghyjgEQVnoWtKAG_oHnuQRQE30H/view?usp=sharing"
                    ,"Recovered":str(randint(10,50000)),"Infected":str(randint(50000,8090000)),"Deaths":str(randint(50,8000)),"Vaccinations":str(randint(90000,8090000))
                 ,"News":"https://www.healthline.com/health-news/how-covid-19-surge-is-related-to-a-black-fungus-outbreak"})
#,"Test Center":"Number 1","Free Slots":"None","Center img":"LINK","Recovered":"10","infected":"100000"




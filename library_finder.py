import pandas as pd
import re
#["City","Country","Country ID","Test Center","Free Slots","Center img","Recovered","Infected", 'Deaths','Vaccinations','News]

###############################TASKS######################################################
##### 1. regenrate new data with vacination and deaths included to data
##### 2. try media (1 hour and after lab3)
######### Free slot ###########
def available(city):
    data = pd.read_csv("https://raw.githubusercontent.com/binHarby/asgroup5/master/dataNew.csv",header=0,encoding='unicode_escape')
    mask = list()
    for record in data['City'].str.lower().str.strip():
        mask.append(bool(re.search(city,record)))
    return data.loc[mask,["City","Test Center","Free Slots"]]
######### Info ###########

def info1(country):
    data = pd.read_csv("https://raw.githubusercontent.com/binHarby/asgroup5/master/dataNew.csv",header=0,encoding='unicode_escape')
    mask = list(bool(re.search(country,record)) for record in data['Country'].str.lower().str.strip())
    data=data[mask &(data['Country'].str.lower().str.strip()==country)]
    return data.reindex(columns=['Recovered','Infected','Deaths','Vaccinations'])
def news(country):
    data = pd.read_csv("https://raw.githubusercontent.com/binHarby/asgroup5/master/dataNew.csv",header=0,encoding='unicode_escape')
    mask = list(bool(re.search(country,record)) for record in data['Country'].str.lower().str.strip())
    data=data[mask &(data['Country'].str.lower().str.strip()==country)]
    data=data.reindex(columns=['News'])
    return data.loc[0,][0]
def imgg(city,center):
    data = pd.read_csv("https://raw.githubusercontent.com/binHarby/asgroup5/master/dataNew.csv",header=0,encoding='unicode_escape')
    mask = list(bool(re.search(city,record)) for record in data['City'].str.lower().str.strip())
    data=data[mask &(data['City'].str.lower().str.strip()==city)&(data['Test Center'].str.lower().str.strip()=='center' +str(center))]
    data=data.reindex(columns=['Center img'])
    return (data.loc[:,][:1-len(data)]).to_string()


######### manual ###########
def manual():
    rs="============================================"
    rs=rs+"\n"+"Commands:\n"+"Get statistics about COVID-19 in your country: info <country_name>\nCheck availablity of test centers near you: available <city_name>\n" 
    rs=rs+"get this very helpful manual: ?\n"+"============================================"
    return rs
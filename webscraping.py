from bs4 import BeautifulSoup as bs
import requests
import csv
url = 'https://www.joblist.com/ca/search?l=Edmonton%2C+AB&q=receptionist&lr=WITHIN_25_KMS'
website = requests.get(url)
soup = bs(website.content,'html.parser')

all = soup.find_all("div",{"class":"itemUi"})

file = open('jobdetail.csv','w')
writer = csv.writer(file)
writer.writerow(['TITLE','COMPANY NAME','LOCATION'])
for i in all:
    title = i.find_all("h2",{"class":"itemHeaderUi css-10w5g4p"})[0].text
    companyname = i.find_all("div",{"class":"itemMetaUi css-11t701e"})[0].text
    location = i.find_all("div",{"class":"itemMetaUi css-gbogy6"})[0].text
    print("TITLE: ",title,'\n',"COMPANY NAME: ",companyname,'\n',"LOCATION: ",location,'\n\n')
    writer.writerow([title,companyname,location])
file.close()
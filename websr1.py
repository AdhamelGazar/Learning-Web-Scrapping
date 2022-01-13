# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:56:09 2022

@author: Adham
"""

# 1) installing  el modules

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title= []
company_name=[]
location =[]
skills = []
links = []
salary=[]
# 2) use requests 3shan ngeeb el url
result = requests.get("https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=machine%20learning")

# 3) save el page (content / markup)
src = result.content
#print(src)

# 4)create the soup object to parse content
soup = BeautifulSoup(src,"lxml")
#print(soup)

# 5) find he elements containing infowe need
#-- job titles, job skills , company names , location
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a",{"class":"css-17s97q8"})
locations_names=soup.find_all("span",{"class":"css-5wys0k"})
job_skills=soup.find_all("a",{"class":"css-o171kl"})
#print(job_titles)
#print(company_names)
#print(locations_names)
#print(job_skills)

# 6) loop over returnd list to extract needed info
for i in range((len(job_titles))):
  job_title.append(job_titles[i].text)
  links.append(job_titles[i].find("a").attrs["href"])
  company_name.append(company_names[i].text)
  location.append(locations_names[i].text)
  skills.append(job_skills[i].text)
  
  
for link in links :
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src,"lxml")
    salaries = soup.find("div","css-rcl8e5","span",{"class":"css-4xky9y"})
    salary.append(salaries.text)







#print(job_title)
#print(company_name)
#print(location)
#print(skills)


# 7) create a csv file and fill it with the values

file_list = [job_title,company_name,location,skills,links,salary]
exported = zip_longest(*file_list)
with open("C:\\Users\m\Desktop\webscr1.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company name","location","skills","links","salary"])
    wr.writerows(exported)


# 8) get the salries and requirment


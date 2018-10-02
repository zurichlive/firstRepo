#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[47]:


r = requests.get('https://www.ecb.europa.eu/home/html/index.en.html')
soup = BeautifulSoup(r.text, 'html.parser')
alist = []
blist = []
text = soup.find_all('td', {'class':'stats-table-figure'})
percentage = soup.find_all('td', {'class':'stats-table-percentage'})

for element1, element2 in zip (text, percentage):
    # list in list (replace unwanted characters)
    alist.append([element1.text,element2.text.replace("\xa0%","")])
    # dictionary in list (and replace unwanted characters)
    #blist.append({element1.text.replace("\xa0%",""):element2.text.replace("\xa0%","")})
    minidict = {'Title':element1.text,'Percentage':element2.text.replace('\xa0','')}
    blist.append(minidict)
    


# In[ ]:





# In[49]:


data = pd.DataFrame(alist)
print(data)
data.to_csv("ezb_list_list.csv")
data2 = pd.DataFrame(blist)
print(data2)
data2.to_csv("ezb_list_dict.csv")


# In[ ]:





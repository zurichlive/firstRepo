#!/usr/bin/env python
# coding: utf-8

# In[52]:


from bs4 import BeautifulSoup
import pandas as pd
import os


# In[53]:


## This method loads html, processes them and creates csv
##
##
##


# In[ ]:





# In[44]:


# returns string without evil characters
#
#
def make_beautiful(temp_string):
    temp_string = temp_string.replace('<br><br>','<br>')
    temp_string = temp_string.replace('<br>','; ').replace('<td>','').replace('</br>','').replace('</td>','').replace('<br/>','').replace('<td/>','').strip()
    if temp_string[len(temp_string)-1] == ';':
        temp_string =  temp_string[:-1]
    temp_string = temp_string.replace(':;',':')
    temp_string = temp_string.replace(' ;',';')
    temp_string = temp_string.replace(',;',',')
    temp_string = temp_string.replace('.;','.')
    temp_string = temp_string.replace('!;','!')
    temp_string = temp_string.replace('?;','?')
    temp_string = temp_string.replace('&amp;','&')
    temp_string = " ".join(temp_string.split())
    return temp_string


# In[54]:


# returns list with admin.ch-Veranstaltung details of id provided
# 
#
def process_html(event_id):
    f = open("html/"+str(event_id)+".html", 'r')
    r = BeautifulSoup(f.read(), 'html.parser')
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    dic = {}
    for elem in r.find_all('tr'):
        Key = elem.find('th').text.strip()
        Value = elem.find('td').text.strip()
        Value = make_beautiful(Value)
        Value = Value.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()
        
        minidict = {Key:Value}
        dic.update(minidict)
    # add id
    Key = 'ID'
    Value = event_id
    minidict = {Key:Value}
    dic.update(minidict)
    # add url
    Key = 'URL'
    Value = 'https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.event-id-'+event_id+'.html'
    minidict = {Key:Value}
    dic.update(minidict)

    return dic


# In[ ]:





# In[55]:


#List all the html files and create csv files for them
lst = os.listdir('html')
for htm in lst:
    if "html" in htm: 
        event_id = htm.split(".")[0]
        dic = process_html(event_id)
        dic.update({'File':htm})
        pd.DataFrame([dic]).to_csv("csvs/"+event_id+".csv", index=False) 


# In[ ]:





# In[ ]:





# In[ ]:





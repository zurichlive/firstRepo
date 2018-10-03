#!/usr/bin/env python
# coding: utf-8

# In[201]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


# In[202]:


url_base = 'https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.event-id-'
url_end = '.html'


# In[205]:


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

# returns list with admin.ch-Veranstaltung details of id provided
# 0 = Ort
# 1 = Zeit
# 2 = Beschreibung
# 3 = Kontakt
# 4 = Veranstalter
# 5 = URL
#
#
def get_detail(event_id):
    url = url_base + str(event_id) + url_end
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all('td',{'class':''})
    result_list = []
    
    # 0 = Ort
    # 1 = Zeit
    # 2 = Beschreibung
    # 3 = Kontakt
    # 4 = Veranstalter
    try:
        result_time = result[1].text.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()
        result_who = result[4].text.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()

        # make sure that new line character is preserved so that text is formatted
        # replace new line with ";"
        result_place = make_beautiful(str(result[0]))
        result_desc = make_beautiful(str(result[2]))
        result_contact = make_beautiful(str(result[3]))
        #result_place = result[0].text.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()
        #result_desc = result[2].text.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()
        #result_contact = result[3].text.replace('\xa0',' ').replace('\t','').replace('\n',' ').strip()
        
        result_list.append(result_place)
        result_list.append(result_time)
        result_list.append(result_desc)
        result_list.append(result_contact)
        result_list.append(result_who)
        result_list.append(url)
    except IndexError:
        print('IndexError with id '+str(event_id))
    #except:
    #    print('General error with id'+str(event_id))
        
    return result_list


# In[206]:


# get Veranstaltungen
#
#
result_list = []

# user input
#
print("*** Get Veranstaltungs-Detail from admin.ch ***")
print("*** Please provide ids")
start_input = input("Start id: ")
end_input = input("End id (leave empty if only one id is needed): ")

start_id = int(start_input)

# if user input of end_id is empty we only get the single id provided
#
if end_input is '':
    new_list = get_detail(start_id)
    if len(new_list)>0:
        result_list.append(new_list)
else:
    # else we get the whole range
    #
    end_id = int(end_input) 
    
    # loop through range
    #
    for x in range(start_id,end_id):
        new_list = get_detail(x)
        if len(new_list)>0:
            result_list.append(new_list)


# with panda convert list and write to csv
#

print('*** Thank you - we are done with Veranstaltungen from admin.ch ***')
data = pd.DataFrame(result_list)
data.to_csv("veranstaltungen" + str(random.randrange(0, 10000)) + str(random.randrange(0, 10000)) + ".csv")


# In[ ]:





# In[ ]:





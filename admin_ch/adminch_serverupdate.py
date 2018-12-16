#!/usr/bin/env python
# coding: utf-8

# In[60]:


import requests
from bs4 import BeautifulSoup
import os


# In[61]:


## This program checks for new Veranstaltungen on admin.ch
## It offers the same functionality as the local program 
## But instead of a user input it starts with the latest already 
## scraped Veranstaltung and checks if newer ones are available


# In[62]:


# Saving off the html code into a folder
#
#
def get_detail_new(event_id):
    # get html site for id
    r = requests.get('https://www.admin.ch/gov/de/start/dokumentation/veranstaltungen.event-id-'+str(event_id)+'.html')
    soup = BeautifulSoup(r.text, 'html.parser')
    r = BeautifulSoup(r.text, 'html.parser')
    r = r.prettify("utf-8")
    
    # get title to check if there is a result
    result_title = soup.find_all('h1')
    try:
        # if there is not a result we return empty
        if result_title[0].text.strip() == 'Veranstaltung nicht gefunden':
            print('No Veranstaltung with id '+str(event_id))
            return False
    except IndexError as e:
        print(e)
        print(result_title)

    
    # otherwise we save the html file locally
    with open("html/"+str(event_id)+".html", "wb") as file:
        print('Success! '+str(event_id))
        file.write(r)
        file.close()
        return True


# In[63]:


# Extract the number (id) from the file name list element
#
#
def extract_number(element):
    return int(element.split('.')[0])


# In[66]:


# read latest id that we already have stored as csv and start from there
#

lst = os.listdir('csvs')
lst.remove('.DS_Store')
number_of_runs = 100

if len(lst)<1:
    exit()

start_id = int(max(lst,key=extract_number).split('.')[0])+1
end_id = start_id+number_of_runs
success = False

# check for new Veranstaltungen
for x in range(start_id,end_id):
    success = False
    if get_detail_new(x):
        success = True

# if there are more we go again for the loop
if success:
    start_id = end_id
    end_id = start_id + number_of_runs
    
    # check for new Veranstaltungen
    for x in range(start_id,end_id):
        get_detail_new(x)


# In[37]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup


# In[13]:


## This program gets the html of Veranstaltung id provided and saves them locally
##
##


# In[14]:


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
            return
    except IndexError as e:
        print(e)
        print(result_title)

    
    # otherwise we save the html file locally
    with open("html/"+str(event_id)+".html", "wb") as file:
        print('Success! '+str(event_id))
        file.write(r)
        file.close()


# In[20]:


# user input
#
print("*** Get Veranstaltungs-Detail from admin.ch ***")
print("*** Please provide ids")
start_input = input("Start id: ")
end_input = input("End id (leave empty if only one id is needed): ")

start_id = int(start_input)
counter = 0

# if user input of end_id is empty we only get the single id provided
#
if end_input is '':
    get_detail_new(start_id)

else:
    # else we get the whole range
    #
    end_id = int(end_input) 
    # loop through range
    #
    for x in range(start_id,end_id):
        get_detail_new(x)
        counter = counter + 1

print('*** Thank you - we are done with Veranstaltungen from admin.ch ***')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import os
import datetime


# In[102]:


## Reads the csvs and cleans it
##
##


# In[103]:


#Merging all of the csvs
lst = os.listdir('csvs')
df = pd.DataFrame()
for elem in lst:
    new = pd.read_csv('csvs/'+elem)
    df = pd.concat([df, new],sort=True)
df = pd.DataFrame(df)
#df


# In[104]:


df.describe()


# In[105]:


df.dtypes


# In[106]:


# cleaning
del df['Unnamed: 0']
df = df.rename(columns={'Datum\n           \n           Zeit': 'Datum Zeit'})


# In[107]:


# set a proper index
df['ID'] = df['ID'].astype(int) 
df.set_index('ID', inplace=True)
df = df.sort_index()


# In[110]:


#df[df['Datum Zeit'].isna()]
#df[df['Datum'].notnull()].count()


# In[111]:


# Combine Datum and Datum Zeit
df['Datum'].fillna(df['Datum Zeit'], inplace=True)


# In[112]:


del df['Datum Zeit']


# In[113]:


#df['Datum'].head(20)


# In[114]:


# methods for returning clean date from messy date
#
#
def dateconverter(date_raw):
    date_clean = date_raw[3:13]
    return date_clean

def yearconverter(date):
    year = date.year
    return year

def monthconverter(date):
    month = date.month
    return month

def dayconverter(date):
    day = date.day
    return day


# In[115]:


df['New_Date'] = df['Datum'].apply(dateconverter)
df['New_Date'] = pd.to_datetime(df['New_Date'], format="%d.%m.%Y")


# In[91]:


df.dtypes


# In[ ]:


df['Year'] = df['New_Date'].apply(yearconverter)
df['Month'] = df['New_Date'].apply(monthconverter)
df['Day'] = df['New_Date'].apply(dayconverter)


# In[ ]:





# In[116]:


# cleaning some of the Veranstalter data


# In[122]:


#df['Veranstalter'].value_counts().head(100)


# In[118]:


clean_names = {
    'FDP.Die Liberalen': 'FDP Schweiz',
    'FDP. Die Liberalen': 'FDP Schweiz',
    'SVP UDC': 'SVP Schweiz',
    'SVP': 'SVP Schweiz',
    'Sozialdemokratische Partei der Schweiz SPS': 'SP Schweiz',
    'Sozialdemokratische Partei der Schweiz': 'SP Schweiz',
    'SPS': 'SP Schweiz',
    'SPS/PSS': 'SP Schweiz',
    'SP-Bundeshausfraktion': 'SP-Fraktion',
    'Schweizerischer Gewerkschaftsbund (SGB)': 'Schweizerischer Gewerkschaftsbund SGB',
    'Schweizerischer Gewerkschaftsbund': 'Schweizerischer Gewerkschaftsbund SGB',
    'Grüne - Les Verts':'Grüne Partei der Schweiz',
    'Grüne Partei Schweiz': 'Grüne Partei der Schweiz', 
    'Grüne /Les Verts': 'Grüne Partei der Schweiz', 
    'Grüne': 'Grüne Partei der Schweiz', 
    'Grüne Partei Schweiz (GPS)': 'Grüne Partei der Schweiz', 
    'Grüne Schweiz': 'Grüne Partei der Schweiz', 
    'Grüne Schweiz / Les Verts': 'Grüne Partei der Schweiz', 
    'Grüne Schweiz Partei der Schweiz': 'Grüne Partei der Schweiz', 
    'Grüne Schweiz/Les Verts': 'Grüne Partei der Schweiz', 
    'Grüne.ch': 'Grüne Partei der Schweiz', 
    'Grüne/Les Verts': 'Grüne Partei der Schweiz', 
    'Schweizerischer Gewerbeverband SGV': 'Schweizerischer Gewerbeverband sgv',
    'Schweizerischer Gewerbeverband': 'Schweizerischer Gewerbeverband sgv',
    'Schweiz. Gewerbeverband': 'Schweizerischer Gewerbeverband sgv',
    'Schweiz. Gewerbeverband SGV': 'Schweizerischer Gewerbeverband sgv',
    'Schweiz. Gewerbeverband sgv': 'Schweizerischer Gewerbeverband sgv',
    'Allianz der Konsumentenschutz-Organisationen': 'Allianz der Konsumentenschutz-Organisationen (SKS)',
    'Amtliche Vermessung': 'Amtliche Vermessung Schweiz',
    'AUNS Schweiz': 'AUNS',
    'Bundesamt für Energie': 'Bundesamt für Energie (BFE)',
    'Bundesamt für Landwirtschaft BLW': 'Bundesamt für Landwirtschaft',
    'Bundesamt für Sport': 'Bundesamt für Sport BASPO',
    'Bundesamt für Statistik': 'Bundesamt für Statistik BFS',
    'Büro des Nationalrates': 'Büro-N',
    'CVP': 'CVP Schweiz',
    'CVP/PDC': 'CVP Schweiz',
    'CVP-Bundeshausfraktion':'CVP-Fraktion',
    'Die Post': 'Die Schweizerische Post',
    'économiesuisse': 'economiesuisse',
    'Economisuisse': 'economiesuisse',
    'Eidg. Kommission gegen Rassismus (EKR)': 'Eidg. Kommission gegen Rassismus EKR',
    'Eidg. Kommission gegen Rassismus ERK': 'Eidg. Kommission gegen Rassismus EKR',
    'Eidg. Kommunikationskommission (ComCom)': 'Eidg. Kommunikationskommission ComCom',
    'Eidgenössische Elektrizitätskommission': 'Eidgenössische Elektrizitätskommission ElCom',
    'Eidgenössische Finanzmarktaufsicht (FINMA)': 'Eidgenössische Finanzmarktaufsicht FINMA',
    'Eidgenössisches Departement des Innern': 'Eidgenössisches Departement des Innern (EDI)',
    'Eidgenössisches Departement für Wirtschaft, Bildung und Forschung': 'Eidgenössisches Departement für Wirtschaft, Bildung und Forschung WBF',
    'Eidgenössisches Departement für Wirtschaft, Bildung und Forschung (WBF)': 'Eidgenössisches Departement für Wirtschaft, Bildung und Forschung WBF',
    'Eidgenössisches Justiz- und Polizeidepartement': 'Eidgenössisches Justiz- und Polizeidepartement EJPD',
    'FDP': 'FDP Schweiz',
    'FDP Die Liberalen': 'FDP Schweiz',
    'FPD.Die Liberalen': 'FDP Schweiz',
    'Fraktion CVP': 'CVP Fraktion',
    'Fraktion CVP-EVP-glp': 'CVP-EVP-glp Fraktion',
    'Gewerkschaft UNIA Bern': 'Gewerkschaft UNIA',
    'Unia': 'Gewerkschaft UNIA',
    'UNIA': 'Gewerkschaft UNIA',
    'interpharma iph': 'Interpharma',
    'JCVP Schweiz': 'JCVP',
    'Junge Grüne Schweiz': 'Junge Grüne',
    'Jungfreisinnige': 'Jungfreisinnige Schweiz',
    'jungfreisinnige Schweiz': 'Jungfreisinnige Schweiz',
    'Jungfreisinnige Schweiz (jfs)': 'Jungfreisinnige Schweiz',
    'jungfreisinnige schweiz jfs': 'Jungfreisinnige Schweiz',
    'Jungsozialistinnen Schweiz (JUSO)': 'JUSO',
    'JUSO Schweiz': 'JUSO',
    'Parlamentesdienste': 'Parlamentsdienste',
    'Schweizerische Volkspartei': 'SVP Schweiz',
    'Schweizerische Volkspartei SVP': 'SVP Schweiz',
    'SVP/UDC': 'SVP Schweiz'
}
df['Veranstalter'].replace(clean_names, inplace=True)


# In[119]:


# Export Organisator names as csv
#
#data = pd.DataFrame(df_all.Organisator.unique())
#data.to_csv("unique_names2.csv")


# In[123]:


#df['Veranstalter'].value_counts()


# In[121]:





# In[ ]:


# Saving the cleaned csv as "working.csv" for further analysis
df.to_csv("working.csv", index=False) 
#df.to_csv("veranstaltungen_clean_ date_"+str(datetime.datetime.now().strftime("%Y-%m-%d"))+".csv")


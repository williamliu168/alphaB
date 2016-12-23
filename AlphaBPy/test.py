import requests
import pprint as pp
import pandas as pd
import numpy as np
# from morris import * # api username and password

def api_getData(in_url, in_params, in_username, in_password):
    r = requests.get(in_url,params=in_params, auth=(in_username,in_password))
    if 'errors' in r.json():
        errors = r.json()['errors']
        for error in errors:
            print (error['human'])
    return r

#Setting
url_base = "https://api.intrinio.com/"
url_fundamentals = "fundamentals/standardized"
url_statement = "financials/standardized"

#Authentication
api_username = "fc91454b73015ba84d313c64b4244094"
api_password = "35cd4fce4a82958d88590e4765696c46"

ticker = "LB"

p = {'identifier':ticker,'statement':'income_statement','type':'QTR'}
r = api_getData(url_base+url_fundamentals,p,api_username,api_password)

dates = r.json()['data']

df = pd.DataFrame()
for dates_element in dates[:2]:
    date = dates_element['end_date']
    #print(date)
    p = {'identifier':ticker,'statement':'income_statement','type':'QTR','date':date}
    r = requests.get(url_base+url_statement, params=p, auth=(api_username, api_password))
    
    data = pd.Series()
    data.columns=[date]
    result = r.json()['data']
    for keyValuePair in result:
        data[keyValuePair['tag']] = keyValuePair['value']
    print(data)
    #print(data.index)
    #print(data.columns)

    frames = [df,data]
    df=pd.concat(frames, axis=1)
    #df[date] = data
df.head()
    

    
    
    
    
    
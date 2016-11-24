import pandas as pd
import numpy as np
import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
import quandl
from time import gmtime, strftime

feedType = "SF0"

# "KCAP"
# "KE"
# "KEGX"
symbolList = ["KCAP","KE","KEGX"]
indicatorList = [   'REVENUE','REVENUEUSD','COR','GP','RND','SGNA','EBIT','EBITUSD','INTEXP','EBT','TAXEXP','NETINC','PREFDIVIS',   \
                    'NETINCCMN','NETINCCMNUSD','NETINCDIS','EPS','EPSUSD','EPSDIL','SHARESWA','SHARESWADIL','DPS','NCFO','DEPAMOR', \
                    'NCFI','CAPEX','NCFF','NCFDEBT','NCFCOMMON','NCFDIV','NCFX','NCF','ASSETS','ASSETSC','ASSETSNC','CASHNEQ',      \
                    'CASHNEQUSD','RECEIVABLES','INTANGIBLES','INVENTORY','LIABILITIES','LIABILITIESC','LIABILITIESNC','DEBT',       \
                    'DEBTUSD','PAYABLES','EQUITY','EQUITYUSD','RETEARN','ACCOCI','BVPS','CURRENTRATIO','DE','DILUTIONRATIO',        \
                    'EBITDA','EBITDAUSD','FCF','FCFPS','INVCAP','TANGIBLES','TBVPS','WORKINGCAPITAL']

quandl.ApiConfig.api_key='zcxKTeTbMQ5nPdeoPQoR'

#dict = {}

for symbol in symbolList:
    #content = {}
    #dict[symbol]=content
    #print("[SYMBOL] "+symbol);
    
    # list of df
    df = pd.DataFrame()
    for indicator in indicatorList:
        # print("[INDICT] "+indicator);
        
        queryString = feedType+"/"+symbol+"_"+indicator+"_MRY";
        data = quandl.get(queryString);
        # content[indicator]=data
        # data.set_index(indicator)
        data.columns=[indicator]
        
        # print(data)
        frames = [df,data]
        df=pd.concat(frames, axis=1)
        
        
    #print(df)
    fileName="C:\\Users\\wiliu\\Desktop\\alphaB\\generated\\"+feedType+"_"+symbol+".csv"
    df.to_csv(fileName, sep='|')
    nowtime = strftime("%H:%M:%S", gmtime())
    print("["+nowtime+"] Written to file: "+fileName)
        
# print(dict['MOGA']['REVENUEUSD'])
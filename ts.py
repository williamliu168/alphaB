import pandas as pd
import numpy as np
import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
import quandl

symbolList = ['DIS','JNJ','KO']
indicatorList = ['REVENUE']

quandl.ApiConfig.api_key='zcxKTeTbMQ5nPdeoPQoR'

dict = {}

for symbol in symbolList:
    content = {}
    dict[symbol]=content
    # print("[SYMBOL] "+symbol);
    for indicator in indicatorList:
        # print("[INDICT] "+indicator);
        
        queryString = "SF1/"+symbol+"_"+indicator+"_MRY";
        data = quandl.get(queryString);
        # print (data)
        content[indicator]=data
        #print(data.head())

print(dict['DIS']['REVENUE'])
# for data in dict['DIS']['REVENUE']:
#    print(data)
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
import quandl
from time import gmtime, strftime

feedType = "SF1"

symbolList = ["HD"]
#indicatorList = ["REVENUE","REVENUEUSD","COR","GP","RND","SGNA","OPEX","OPINC","EBIT","EBITUSD","INTEXP","TAXEXP","CONSOLINC","NETINCNCI","NETINC","PREFDIVIS","NETINCCMN","NETINCCMNUSD","NETINCDIS","EPS","EPSUSD","EPSDIL","SHARESWA","SHARESWADIL","DPS","NCFO","DEPAMOR","SBCOMP","NCFI","CAPEX","NCFBUS","NCFINV","NCFF","NCFDEBT","NCFCOMMON","NCFDIV","NCFX","NCF","ASSETS","ASSETSC","ASSETSNC","CASHNEQ","CASHNEQUSD","RECEIVABLES","INTANGIBLES","INVENTORY","LIABILITIES","LIABILITIESC","LIABILITIESNC","DEBT","DEBTUSD","DEBTC","DEBTNC","DEFERREDREV","DEPOSITS","INVESTMENTS","INVESTMENTSC","INVESTMENTSNC","PAYABLES","PPNENET","TAXASSETS","TAXLIABILITIES","EQUITY","EQUITYUSD","RETEARN","ACCOCI","ASSETTURNOVER","ASSETSAVG","BVPS","CURRENTRATIO","DE","DIVYIELD","EBITDA","EBITDAUSD","EBITDAMARGIN","EBT","EQUITYAVG","EV","EVEBIT","EVEBITDA","FCF","FCFPS","FXUSD","GROSSMARGIN","INVCAP","INVCAPAVG","MARKETCAP","NETMARGIN","PE","PE1","PS1","PS","PB","ROIC","SPS","PAYOUTRATIO","ROA","ROE","ROS","TANGIBLES","TBVPS","WORKINGCAPITAL","PRICE","SHAREFACTOR","SHARESBAS","TICKER","DIMENSION","CALENDARDATE","DATEKEY","REPORTPERIOD","EVENT"]

indicatorList = ["REVENUE","ASSETS","CAPEX","GP","EQUITY","EPS"]

quandl.ApiConfig.api_key='zcxKTeTbMQ5nPdeoPQoR'

#dict = {}

for symbol in symbolList:
    #content = {}
    #dict[symbol]=content
    #print("[SYMBOL] "+symbol);
    
    # list of df
    df = pd.DataFrame()
    for indicator in indicatorList:
        print("[INDICT] "+indicator);
        
        queryString = feedType+"/"+symbol+"_"+indicator+"_MRQ";
        data = quandl.get(queryString);
        # content[indicator]=data
        # data.set_index(indicator)
        data.columns=[indicator]
        
        print(data)
        frames = [df,data]
        df=pd.concat(frames, axis=1)

    #print(df)
    fileName="C:\\Users\\wiliu\\Desktop\\alphaB\\generated\\"+feedType+"\\"+symbol+".csv"
    df.to_csv(fileName, sep='|')
    nowtime = strftime("%H:%M:%S", gmtime())
    print("["+nowtime+"] Written to file: "+fileName)

 #print(dict['HD']['REVENUEUSD'])
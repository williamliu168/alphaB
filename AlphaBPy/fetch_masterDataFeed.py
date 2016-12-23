import pprint as pp
import pandas as pd
import numpy as np
import csv
# from morris import * # api username and password
import intrinio.api as api

p = {}#{'page_size':2000,'page_number':1}
data = api.getData(intrinio.api.url_base+"companies",p)

f = csv.writer(open('MasterDataFeed.csv','w'))

f.writerow(["ticker", "name", "lei", "cik"])
for x in data:
    f.writerow([
                    x["ticker"],
                    x["name"],
                    x["lei"],
                    x["cik"]
                ])
    

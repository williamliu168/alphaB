import pandas as pd
import numpy as np
import glob

list = glob.glob('./generated/SF0_*.csv')

grand = pd.DataFrame()
for file in list:
    data = pd.read_csv(file, sep='|')
    symbol = file.split('.')[1].split('_')[1]
    print(symbol)
    d = pd.DataFrame(symbol, index=np.arange(len(data)), columns=['SYMBOL'])

    data = d.join(data)
    grand = grand.append(data)
    
    
print(grand)
outFile="grand.csv"
grand.to_csv(outFile, sep='|')
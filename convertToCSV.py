import pandas as pd
import numpy as np
import csv
import re
import os


directory = './Data/Stocks'
files = os.listdir(directory)
index = 0
while index < 10:
    filename = files[index]
    if filename.endswith('.txt'):
        # print(filename+' - '+filename[:-7])
        file = pd.read_fwf(directory+'/'+filename)
        # with open(os.path.join(directory, filename)) as f:
        #     print(f.read())
        file.to_csv('./Stocks/'+filename[:-7]+'.csv',index=None) 
    index += 1



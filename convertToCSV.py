import pandas as pd
import numpy as np
import csv
import re
import os


directory = './Kaggle/Data/Stocks'
files = os.listdir(directory)
index = 0
while index < 2:
    filename = files[index]
    if filename.endswith('.txt'):
        print(filename+' - '+filename[:-7])
        # file = pd.read_fwf(directory+'/'+filename)
        # with open(os.path.join(directory, filename)) as f:
        #     print(f.read())

        with open(os.path.join(directory, filename)) as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)
            with open('./Stocks/'+filename[:-7]+'.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)
        # file.to_csv('./Stocks/'+filename[:-7]+'.csv',index=None) 
    index += 1
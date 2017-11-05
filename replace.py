#!/usr/bin/env python

# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
def replace(name):
    rf = pd.read_excel('/Users/BuleSky/Desktop/OMG/'+name+'.xlsx',header=1)
    link1 = list(rf.columns)
    np_link1 = np.array(link1)
#print(link1)
    link2 = rf.values
#print(link2)
    values = np.vstack((np_link1, link2))

    print(values)



# print(rf)
    df = pd.DataFrame(values,columns=['time',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
#print(df)
    df.to_csv('/Users/BuleSky/Desktop/OMG/'+name+'1.csv',index=False)
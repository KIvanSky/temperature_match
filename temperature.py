# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:28:12 2017

"""

# !/usr/bin/python
# coding:utf-8
# !/usr/bin/python
# coding:utf-8
import pandas as pd

from temperature_match import replace as r

data_name = ["719-721result"]
data = None
for name in data_name:
    r.replace(name)
    if name == data_name:
        data = pd.read_csv('/Users/BuleSky/Desktop/OMG/'+ name + "1.csv")
    else:

        data = pd.concat([data,pd.read_csv('/Users/BuleSky/Desktop/OMG/'+name + "1.csv")])
#print(data)
data.index = range(0, len(data))
#print(data.index)
data["float_time"] = data.time.apply(lambda t: float(t[6:10] + t[3:5] + t[:2] +t[11:13] + t[14:16] + t[17:19]))
#print(data["float_time"])
result = pd.read_excel("/Users/BuleSky/Desktop/OMG/result.xlsx").fillna(0)[:]
#print(result)
count = 0
time_count = 0
for i in result.index:
    print(i)
    start = result.iloc[i].picturename
    end = start + 1

    print(start)
    print(end)
    print(type(data.float_time))
    if len(data.index[(data.float_time >= start) & (data.float_time <= end)]) > 0:
        time_count = 0
    else:
        time_count += 1
    count += len(data.index[(data.float_time >= start) & (data.float_time <= end)])
    #data.index[(data.float_time >= start) & (data.float_time <= start + 1)]:
    data.loc[data.index[(data.float_time >= start) & (data.float_time <= end)], '30'] = result.iloc[i].right
    data.loc[data.index[(data.float_time >= start) & (data.float_time <= end)], '31'] = result.iloc[i].left

data = data.loc[list(data.loc[:, ['30', '31']].dropna(axis=0).index), :]
#ata = data.drop(['float_time', 'Unnamed: 30'], axis = 1)
data = data.drop(['float_time'], axis=1)
data.to_csv("/Users/BuleSky/Desktop/OMG/result.csv", index = False)
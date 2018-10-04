#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:51:33 2018

@author: Seanhoy
"""
import requests 
import datetime
import matplotlib
import matplotlib.pyplot as plt

#Url retrieved from grogdata Aug 1 - Aug 7
#https://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,d2w.json?time_col=ReceptionTime&begin=1533117600&end=1533722399
meshlaburl = 'https://grogdata.soest.hawaii.edu/data/2/node-008/ReceptionTime,d2w.json?time_col=ReceptionTime&begin=1533117600&end=1533722399'
print(meshlaburl)
#request.get('google.com')

ml = requests.get(meshlaburl).json()
print ()
print('Got {} samples.'.format(len(ml)))
print(ml)

def d2w2m(x):
    return (1400 - x)/1e3

x, y = tuple(zip(*ml))

x = [datetime.datetime.utcfromtimestamp(tmp) for tmp in x]

plt.figure()
plt.plot_date(x, y, '.-')
plt.xlabel('Local Time')
plt.ylabel('Water Depth, meter')
plt.title('Water Depth of node-046')
plt.grid(True)
plt.show()


#Url retrieved from NOAA Aug 1 - Aug 7
#https://tidesandcurrents.noaa.gov/api/datagetter?product=hourly_height&application=NOS.COOPS.TAC.WL&begin_date=20180801&end_date=20180807&datum=MLLW&station=1612480&time_zone=LST&units=english&format=json
url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=hourly_height&application=NOS.COOPS.TAC.WL&begin_date=20180801&end_date=20180807&datum=MLLW&station=1612480&time_zone=LST&units=english&format=json'
print(url)

r = requests.get(url).json()

type(r)

r.keys()

r['data']

d = r['data']

type(d)

float(d[0]['v'])

d[0]

d[0]['v']

float(d[0]['v'])
#float function converst string to numerical

def feet2meter(foot):
    return 0.3048 * foot

datetime.datetime.strptime(d[0]['t'], '%Y-%m-%d %H:%M')
#import datetime and use above command to change to python readable date time

DT = []
depth = []
for element in d:
    dt = datetime.datetime.strptime(element['t'], '%Y-%m-%d %H:%M')
    v = float(element['v'])
    
    DT.append(dt)
    depth.append(v)
    
import matplotlib.pyplot as plt
plt.plot_date(DT, depth, 'r:.')
plt.show()
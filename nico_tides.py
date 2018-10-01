import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


end = time.time()
days = 30
begin = end-days*86400
node = 'node-046'
var = 'd2w'

urlsoest = 'https://grogdata.soest.hawaii.edu/data/2/{node}/ReceptionTime,{var}.json?begin={begin}&end={end}&time_col=ReceptionTime'
urlsoest = urlsoest.format(begin=begin, end=end, node=node, var=var)

urlnoaa = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date={begin2}end_date={end2}datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'
urlnoaa = urlnoaa.format(begin2=time.strftime('%Y%m%d',time.gmtime(begin))+'&', end2=time.strftime('%Y%m%d',time.gmtime(end))+'&')

soest = requests.get(urlsoest)
soest = soest.json()

dfsoest = pd.DataFrame(soest)
dfsoest = dfsoest.rename(columns={0:'t',1:'SOEST Waterlevel'})
dfsoest['t'] = pd.to_datetime(dfsoest['t'],unit='s')
dfsoest['SOEST Waterlevel'] = 1 - dfsoest['SOEST Waterlevel']/1000

noaa = requests.get(urlnoaa)
noaa = noaa.json()
datnoaa = noaa['data']
dfnoaa = pd.DataFrame(datnoaa)
dfnoaa = dfnoaa.rename(columns={'v':'NOAA Waterlevel'})
dfnoaa['t'] = pd.to_datetime(dfnoaa['t'], format = '%Y-%m-%d %H:%M')
dfnoaa['NOAA Waterlevel'] = pd.to_numeric(dfnoaa['NOAA Waterlevel'])*0.3048

offset = dfnoaa['NOAA Waterlevel'].mean() - dfsoest['SOEST Waterlevel'].mean()
dfsoest['SOEST Waterlevel'] = dfsoest['SOEST Waterlevel'] + offset
dfsoest = pd.merge_asof(dfnoaa, dfsoest, on='t')
dfsoest['Difference'] = (dfsoest['NOAA Waterlevel'] - dfsoest['SOEST Waterlevel']) *1000

plt.figure(1)

ax1 = plt.subplot(211)
plt.plot(dfsoest['t'],dfsoest['SOEST Waterlevel'],'r--')
plt.plot(dfnoaa['t'],dfnoaa['NOAA Waterlevel'],'g--')
plt.legend()
plt.ylabel('waterlevel [m]')
plt.setp(ax1.get_xticklabels(), visible=False)

ax2 = plt.subplot(212, sharex=ax1)
plt.plot(dfsoest['t'],dfsoest['Difference'], 'b--')
plt.legend()
plt.ylabel('NOAA waterlevel\n- SOEST waterlevel\n[mm]')
plt.xlabel('date')

plt.show()



time.strftime('%Y%m%d',time.gmtime(time.time()))

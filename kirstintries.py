import datetime
import requests

url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=hourly_height&application=NOS.COOPS.TAC.WL&begin_date=20180815&end_date=20180915&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'

r = requests.get(url)
r = r.json()

#print(float(r['metadata']['lon']))
#print(r['metadata'] prints the metadata

# defines variable for the data
d = r['data']

# print(r.text) gives one giant string


DT = []
depth = []
for element in d:
#pulls out the date and time
    dt = datetime.datetime.strptime(element['t'], '%Y-%m-%d %H:%M')
#float converts string to a value
    v = float(element['v'])

#append puts something at the end of the list
    DT.append(dt)
#puts v at end of the depth list
    depth.append(v)

import matplotlib.pyplot as pit
pit.plot_date(DT, depth, 'r:.')
pit.show()
import datetime
import requests
import matplotlib.pyplot as plt


url2 = 'http://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,Timestamp,d2w.json?time_col=ReceptionTime&begin=1534291200.0&end=1536969600.0&time_col=ReceptionTime'


r = requests.get(url2)
d = r.json()


DT = []
depth = []
for element in d:

#add functions for both dt and v that convert the time to date time and convert the measurement to actual depth to match that of noaa and compare    
#pulls out the date and time
    dt = element[1]
#float converts string to a value
    v = element[2]

#append puts something at the end of the list
    DT.append(dt)
#puts v at end of the depth list
    depth.append(v)


plt.plot(DT, depth, 'r:.')
plt.show()

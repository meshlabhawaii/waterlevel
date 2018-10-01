import matplotlib.pyplot as plt
f= open('/home/pi/waterlevel.csv')
f. close()

X = []
Y = []

for line in data[0:]:
line = line.split(',')
x = float(line[0])
y = float(line[1])
X.append(x)
Y.append(y)

plt.figure()
plt.title('NOAA Tide Guage VS MESH Lab Tide Guage')
plt.plot(X,Y,'b.-')
plt.xlabel('Timestamp')
plt.ylabel('waterlevel')

plt.show()

plt.savefig('Waterlevel(NOAA VS MESH Lab)')

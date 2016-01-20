import urllib
import json
import sys
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#coor1 = sys.argv[1]
#coor2 = sys.argv[2]
#x = sys.argv[3]
#y = sys.argv[4]
#resolution = sys.arg[5]

cent_coor_1 = 51.933333
cent_coor_2 = 15.5
x_km = 200.0
y_km = 300.0
resolution = 200

key = 'AIzaSyABFgIWxLyVBuH5T4twN2yKdgtJtS67BEM'
x = x_km/110.574
y = y_km/(111.320*np.cos(x))

first_x = cent_coor_1-(x/2)+((x/resolution)/2)
first_y = cent_coor_2+(y/2)-((y/resolution)/2)
last_x = cent_coor_1+(x/2)-((x/resolution)/2)
last_y = cent_coor_2-(y/2)+((y/resolution)/2)

ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json'

array = np.zeros([resolution, resolution])

for loop in range (resolution):
	next_x = first_x+(x/resolution*(loop))
	url = ELEVATION_BASE_URL + '?path=' + str(next_x) + ',' + str(first_y) + '|' + str(next_x) + ',' + str(last_y) + '&samples=' + str(resolution) + '&key=' + key #'
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	#print data
	
	count = 0
	for value in data['results']:
		array[count, loop] = value['elevation']
		count = count + 1
		
	if (loop == resolution-1):
		print next_x
		
print array
		

print data['status']

file = open("output.txt","w")
for loop in range (resolution):
	for loop2 in range (resolution):
		file.write (str(loop) + '\t' + str(loop2) + '\t' + str(array[loop, loop2]) + '\n')
file.close


##plotting
x_list = []
y_list = []
z_list = []

for loop in range (resolution):
	for loop2 in range (resolution):
		x_list.append(loop)
		y_list.append(loop2)
		z_list.append(array[loop, loop2])
file.close


plt.imshow(array)
plt.show()
#ax = plt.figure().gca(projection = '3d')
#ax.plot_surface(x_list, y_list, z_list, rstride = 8, cstride = 8, alpha = 0.3)
#plt.show()

#plt.figure()
#CS = plt.contour(x_list, y_list, z_list)
#plt.clabel(CS, inline = 1, fontsize = 10)





#print first_x
#print first_y
#print last_x
#print last_y

#url = ELEVATION_BASE_URL + '?path=' + str(last_x) + ',' + str(first_y) + '|' + str(last_x) + ',' + str(last_y) + '&samples=' + str(resolution) + '&key=' + key #'
#response = urllib.urlopen(url)
#data = json.loads(response.read())
#print data

#for value in data['results']:
#	print value['elevation']


#convert float to string
#elevation = str(bla) + 'abc'
########
#print 'Elevation = ' + elevation




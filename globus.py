# This program uses the Haversine Formula 
# to calculate the Great Circle Distance 
# between two cities around the globe

import math
import pandas as pd

# Opening and reading the file
p = pd.read_csv("simplemaps_worldcities_basic.csv")

# Defining the user input
user_city1 = raw_input("Please enter the name of your first city: ")
user_country_1 = raw_input("Please enter the name of your first country: ")
user_city2 = raw_input("Please enter the name of your second city: ")
user_country_2 = raw_input("Please enter the name of your second country: ")

# The mathematical calculation of the Great Circle Distance 
def greatCircleDistance(lat1, lon1, lat2, lon2):
	r = 6371 # Radius of the Earth in km

	# Variables
	j1 = math.radians(lat1) 
	j2 = math.radians(lat2)
	hj = math.radians(lat2-lat1)
	hi = math.radians(lon2-lon1)

	# Calculation according to the Haversine Formula
	a = math.sin(hj/2) * math.sin(hj/2) + math.cos(j1) * math.cos(j2) * math.sin(hi/2) * math.sin(hi/2)

	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

	d = r * c

	# Printing out the result
	print("\nThe distance between %s & %s is %d km" % (user_city1, user_city2, d))

# A new dataframe with a subset of p, and has only the rows appertaining to Barcelona
cityA = p[(p['City'] == user_city1) & (p['Country'] == user_country_1)]
cityB = p[(p['City'] == user_city2) & (p['Country'] == user_country_2)]

# Getting the latitude and longitude of the first city
lat1 = cityA.iloc[0]['Lat']
lon1 = cityA.iloc[0]['Lon']

# Getting the latitude and longitude of the second city
lat2 = cityB.iloc[0]['Lat']
lon2 = cityB.iloc[0]['Lon']

# Putting everything together
print greatCircleDistance(lat1, lon1, lat2, lon2)

# Debugging and presenting the result
print("\n%s --> %s" % (user_city1, user_country_1))
print("%s --> %s" % (user_city2, user_country_2))
# This program uses the Haversine Formula 
# to calculate the Great Circle Distance 
# between two cities around the globe

import math
import pandas as pd

# Functions 
def read_database(path):
	pd.read_csv(path)

def capture_user_input():
	raw_input("")

def subset_data(data, city, country):	
	cityX = data[(data['City'] == city) & (data['Country'] == country)]
	calculate_latlon(cityX)

def calculate_latlon(name):
	lat = name.iloc[0]['Lat']
	lon = name.iloc[0]['Lon']

def greatCircleDistance(lat1, lat2, lon1, lon2):
	r = 6371 

	j1 = math.radians(lat1) 
	j2 = math.radians(lat2)
	hj = math.radians(lat2-lat1)
	hi = math.radians(lon2-lon1)

	a = math.sin(hj/2) * math.sin(hj/2) + math.cos(j1) * math.cos(j2) * math.sin(hi/2) * math.sin(hi/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = r * c

	print("\nThe distance between %s & %s is %d km" % (user_city1, user_city2, d))

def display_output(cityA, countryA, cityB, countryB, distance):
	print distance

	print("\n%s --> %s" % (cityA, countryA))
	print("%s --> %s" % (cityB, countryB))


# Reading the database
p = read_database("simplemaps_worldcities_basic.csv")

# Getting the user input [I]
user_city1, user_country_1, user_city2, user_country2 = capture_user_input()

# Calculating the location of the cities
lat1, lon1 = calculate_latlon(p, user_city1, user_country1)
lat2, lon2 = calculate_latlon(p, user_city2, user_country2)

# Calculating the final distance using the Great Circle Distance function
distance = greatCircleDistance(lat1, lon1, lat2, lon2)

# Displaying the result [O]
display_output(user_city1, user_country_1, user_city2, user_country2, distance)
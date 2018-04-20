# This program uses the Haversine Formula 
# to calculate the Great Circle Distance 
# between two cities around the globe

import math
import pandas as pd

# Functions 
def read_database(path):
	pd.read_csv(path)

def capture_input():
	user_city_1 = raw_input("Please enter your first city: ")
	user_country_1 = raw_input("Please enter your first country: ")
	user_city_2 = raw_input("Please enter your second city: ")
	user_country_2 = raw_input("Please enter your second country: ")

	return user_city_1, user_country_1, user_city_2, user_country_2

def calculate_latlon(city):
	lat = city.iloc[0]['Lat']
	lon = city.iloc[0]['Lon']
	print city, lat, lon

def greatCircleDistance(lat1, lat2, lon1, lon2):
	r = 6371 

	j1 = math.radians(lat1) 
	j2 = math.radians(lat2)
	hj = math.radians(lat2-lat1)
	hi = math.radians(lon2-lon1)

	a = math.sin(hj/2) * math.sin(hj/2) + math.cos(j1) * math.cos(j2) * math.sin(hi/2) * math.sin(hi/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = r * c

	print("\nThe distance between %s & %s is %d km" % (user_city_1, user_city_2, d))

def display_output(cityA, countryA, cityB, countryB, distance):
	print distance

	print("\n%s --> %s" % (cityA, countryA))
	print("%s --> %s" % (cityB, countryB))


# Reading the database
p = read_database("simplemaps_worldcities_basic.csv")

# Getting the user input [I]
user_city_1, user_country_1, user_city_2, user_country_2 = capture_input()
print(user_city_1, user_country_1, user_city_2, user_country_2)

# Calculating the location of the cities
cityA = p[(p['City'] == user_city_1) & (p['Country'] == user_country_1)]
print cityA
	
cityB = p[(p['City'] == user_city_2) & (p['Country'] == user_country__2)]
print cityB

calculate_latlon(cityA)
calculate_latlon(cityB)

# Calculating the final distance using the Great Circle Distance function
distance = greatCircleDistance(lat1, lon1, lat2, lon2)

# Displaying the result [O]
display_output(user_city_1, user_country_1, user_city_2, user_country_2, distance)
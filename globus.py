# This program uses the Haversine Formula 
# to calculate the Great Circle Distance 
# between two cities around the globe

import math
import pandas as pd

# Functions 
def read_database(path):
	return pd.read_csv(path)

def capture_input():
	user_city_1 = raw_input("Please enter your first city: ")
	user_country_1 = raw_input("Please enter your first country: ")
	user_city_2 = raw_input("Please enter your second city: ")
	user_country_2 = raw_input("Please enter your second country: ")

	return user_city_1, user_country_1, user_city_2, user_country_2

def subset_data(cityA, countryA, cityB, countryB):
	cityX = p[(p['City'] == cityA) & (p['Country'] == countryA)]
	cityY = p[(p['City'] == cityB) & (p['Country'] == countryB)]

	lat1, lon1 = calculate_latlon(cityX)
	lat2, lon2 = calculate_latlon(cityY)

	return lat1, lon1, lat2, lon2

def calculate_latlon(city):
	lat = city.iloc[0]['Lat']
	lon = city.iloc[0]['Lon']
	return lat, lon

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
	print("\n%s --> %s" % (cityA, countryA))
	print("%s --> %s" % (cityB, countryB))


# Reading the database
p = read_database("simplemaps_worldcities_basic.csv")

# Getting the user input [I]
user_city_1, user_country_1, user_city_2, user_country_2 = capture_input()

# Calculating the location of the cities
lat1, lon1, lat2, lon2 = subset_data(user_city_1, user_country_1, user_city_2, user_country_2)

# Calculating the final distance using the Great Circle Distance function
distance = greatCircleDistance(lat1, lon1, lat2, lon2)

# Displaying the result [O]
display_output(user_city_1, user_country_1, user_city_2, user_country_2, distance)
import unittest
from weather import Weather
weather=Weather()
a=input("enter a location")
location = weather.lookup_by_location(a)
condition = location.condition()
print (condition['text'])

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
    print (forecasts['high'])


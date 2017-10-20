import unittest
from weather import Weather
weather=Weather()
location = weather.lookup_by_location("Halifax")
condition = location.condition()
temp=condition.get('temp')
forecast=location.forecast()
print (condition['text'])

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
    print (forecasts['high'])


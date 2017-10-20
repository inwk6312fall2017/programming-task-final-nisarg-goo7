
from weather import Weather
weather = Weather()
def lookuplocation(city):
    location = weather.lookup_by_location(city)
    print(location)
    condition = location.condition() 

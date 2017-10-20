from weather import Weather
weather = Weather()
#def lookuplocation(city):
location = weather.lookup_by_location('Halifax')
condition = location.condition()
temp=[]
forecasts = location.forecast()
for i in forecasts:
		high=i['high']
		temp.append(int(high))
#	for i in forecasts:
		if int(i['high'])==max(temp):
			print('Day with max tep in next 5 days is %s '% (i['date']))
			print('higest temprature is %s'%(i['high']))
			break

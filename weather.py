import requests as re
    
city = input("Enter city name:")
key = '' #api key
date = input("Enter 1st date format yyyy-mm-dd:")
date2 = input("Enter 2nd date format yyyy-mm-dd:")
url = ("http://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}").format(key,city,date)
url2 = ("http://api.weatherapi.com/v1/history.json?key=e0e95876ccde413788f191824222708&q={}&dt={}").format(city,date2)
data = re.get(url)
temp = data.json()['forecast']['forecastday'][0]['day']['avgtemp_c']
data2 = re.get(url2)
temp2 = data2.json()['forecast']['forecastday'][0]['day']['avgtemp_c']
avg = float(temp) + float(temp2)
avg = avg/2
print("date 1 temprature is : ",temp)
print("date 2 temprature is : ",temp2)
print("average tempature is : {0:.1f}".format(avg))

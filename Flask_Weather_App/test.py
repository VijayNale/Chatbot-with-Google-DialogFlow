import pyowm
owm = pyowm.OWM('ff1407e6378a533d971f9f8c19145828') # TODO: Replace <api_key> with your API key
sf = owm.weather_at_place('San Francisco, US')
weather = sf.get_weather()
print(weather.get_temperature('fahrenheit')['temp'])

from pyowm.exceptions import api_response_error
try:
    owm.weather_at_place(place)
except api_response_error.NotFoundError:
    print('Wrong information, try again and find out mistakes please')
    time.sleep(10)




#gunicorn==20.0.4
import requests

city = input('Which city? ')

# def main():
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=720a008938da034680002df06bcfd367&units=metric'.format(city)

res = requests.get(url)
data = res.json()
print(res)
print(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

description = data['weather'][0]['description']

print('Temperature: ', temp)
print('Wind Speed: {}'.format(wind_speed))
print('Description: {}'.format(description))
# if __name__ == '__main__':
#     print('Pogoda')
#     main()

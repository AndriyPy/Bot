import requests
open_weather_token = "84e3bdd118d81b2da08999fafe081dc9"

def get_weather(city,open_weather_token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data)

        city = data["name"]
        temp = data["main"]["temp"]
        #вологість
        humidity = data["main"]["humidity"]
        #тиск
        pressure = data["main"]["pressure"]
        maxtemp = data["main"]["temp_max"]
        mintemp = data["main"]["temp_min"]
        #вітер
        wind = data["wind"]["speed"]

        peopwth = (f"city: {city}\nhumidity: {humidity}%\npressure: {pressure}\ntemp: {temp}C\nmaxtemp: {maxtemp}C\nmintemp {mintemp}C \nwind {wind}")
        print(peopwth)





    except Exception as ex:
        print("check the city name")


def main():
    city = input("enter the city: ")
    get_weather(city, open_weather_token)



if __name__ == "__main__":
    main()
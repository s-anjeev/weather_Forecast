import requests
import pyfiglet


# title
def print_title(text):
    font = pyfiglet.Figlet()
    title = font.renderText(text)
    print(title)
# current weather
def current_weather(API,API_KEY):
    degree_symbol = '\u00b0'
    user_location = input("Enter your location: ")
    if user_location:
        url = f"{API}{API_KEY}&q={user_location}&aqi=yes"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                name = data['location'].get("name")
                region = data['location'].get("region")
                country = data['location'].get("country")
                print(f"{name}, region:{region}, country:{country}")
                temp = data['current'].get("temp_c")
                text = data['current'].get("condition").get("text")
                cloud = data['current'].get("condition").get("cloud")
                print(f"Current temp:{temp}{degree_symbol}C, weather condition:{text}, cloud:{cloud}")
            else:
                error_data = response.json()
                print(f"Error:{error_data['error'].get('code')}, Error:{error_data['error'].get('message')} ")

        except Exception as e:
            print("Error "+ str(e))
    else:
        print("Error: field cannot be empty")


print_title("Wheather")
API = "https://api.weatherapi.com/v1/current.json?key="
API_KEY = "ec6dc90ed8004f3da5150516242101"
current_weather(API,API_KEY)



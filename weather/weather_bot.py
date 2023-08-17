import requests
from config import tok
from pprint import pprint


def get_weather(tok):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={51.40}&lon={39.12}&appid={tok}")
        data = r.json()
        pprint(data)
    except Exception as ex:
        print(ex)
        print("Что-то пошло не так")


def main():
    get_weather(tok)


if __name__ == '__main__':
    main()

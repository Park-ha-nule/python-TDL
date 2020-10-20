import requests
import datetime
from bs4 import BeautifulSoup

class WeatherService():

    def getWeather():
        def getDate(date):
            return date.text

        def getIconNumber(weather):
            return weather['data-ico'][-1]

        # 웹페이지 요청을 하는 코드. 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
        html = requests.get('https://n.weather.naver.com/today/09140104')

        # 파이썬에서 보기 좋게, 파싱 작업을 거쳐야 각 요소에 접근이 쉬워짐
        # 이것을 도와주는게 beautifulSoup 이다.
        soup = BeautifulSoup(html.text, 'html.parser')

        # 주간예보를 먼저 불러옴 (중복되는 클래스가 있어서 전체로 안하고 주간예보로 먼저 짜르고 시작함)
        data0 = soup.find('div', {'id': 'weekly'})
        print('주간 예보 : ')

        # 주간 예보 안에 내가 필요한 일주일 날씨 박스만 불러옴
        data1 = data0.find('div', {'class': 'scroll_area'})

        # 날짜 불러오기
        date = data1.find_all('span', {'class': 'date'})
        find_date = list(map(getDate, date))

        # 박스안에 날씨 부분 (맑음)이 속한 태그 불러오기
        find_weather = data1.find_all('i', {'class': 'ico _cnLazy'})

        # 리스트 요소번호에 따라 홀수면 오전 날씨, 짝수면 오후 날씨를 나타냄
        find_weather_icon = list(map(getIconNumber, find_weather))
        AMlist = find_weather_icon[0::2]
        PMlist = find_weather_icon[1::2]

        # 오늘 날짜 가져오기
        today = datetime.datetime.today().date()

        # 오늘 시간 가져오기
        todayH = datetime.datetime.today().hour

        result = []
        # 오늘부터 10일뒤에 날짜 불러오기
        for i in range(0, 10):
            tendate = today + datetime.timedelta(days=i)
            result.insert(i, {
                "date": tendate,
                "am": AMlist[i],
                "pm": PMlist[i]
            })

        sunny = [1, 2]
        cloud = [7, 34, 40, 41]
        cloudRain = [8, 9, 10, 15, 27, 29]
        cloudSunny = [3, 4, 5, 6, 17, 20, 25]
        rain = [31, 36, 38]
        snow = [11, 12, 13, 14, 16, 19, 21, 23, 24, 28, 30, 32, 33, 37, 39]
        sunnyRain = [22]
        thunder = [18, 26, 35]

        returnValue = [];
        if todayH < 12:
            weatherli = []
            for i in range(0, 10):
                weather = result[i]['am']
                weatherli.extend(weather)
                intList = list(map(int, weatherli))

            for i in range(0, 10):
                Rweather = intList[i]
                if Rweather in sunny:
                    returnValue.append("sunny")
                elif Rweather in cloud:
                    returnValue.append("cloud")
                elif Rweather in cloudRain:
                    returnValue.append("cloudRain")
                elif Rweather in cloudSunny:
                    returnValue.append("cloudSunny")
                elif Rweather in rain:
                    returnValue.append("rain")
                elif Rweather in snow:
                    returnValue.append("snow")
                elif Rweather in sunnyRain:
                    returnValue.append("sunnyRain")
                else:
                    returnValue.append("thunder")

        else:
            weatherli2 = []
            for i in range(0, 10):
                weather2 = result[i]['pm']
                weatherli2.extend(weather2)
                intList2 = list(map(int, weatherli2))

            for i in range(0, 10):
                Rweather = intList2[i]
                if Rweather in sunny:
                    returnValue.append("sunny")
                elif Rweather in cloud:
                    returnValue.append("cloud")
                elif Rweather in cloudRain:
                    returnValue.append("cloudRain")
                elif Rweather in cloudSunny:
                    returnValue.append("cloudSunny")
                elif Rweather in rain:
                    returnValue.append("rain")
                elif Rweather in snow:
                    returnValue.append("snow")
                elif Rweather in sunnyRain:
                    returnValue.append("sunnyRain")
                else:
                    returnValue.append("thunder")

        return returnValue


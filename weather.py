from bs4 import BeautifulSoup
# pprint 는 딕셔너리의 데이터가 긴 경우에 좀 더 보기 편하게 도와준다.

# img 열기
from PIL import Image
sunnyImg = Image.open('img/sunny.png')
cloudImg = Image.open('img/cloud.png')
rainImg = Image.open('img/rain.png')
cloudRainImg = Image.open('img/cloudRain.png')
cloudSunnyImg = Image.open('img/cloudSunny.png')
snowImg = Image.open('img/snow.png')
sunnyRainImg = Image.open('img/sunnyRain.png')
thunderImg = Image.open('img/thunder.png')

import requests
import datetime

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
data0 = soup.find('div', {'id' : 'weekly'})
print('주간 예보 : ')

# 주간 예보 안에 내가 필요한 일주일 날씨 박스만 불러옴
data1 = data0.find('div', {'class':'scroll_area'})

# 날짜 불러오기
date = data1.find_all('span', {'class' : 'date'})
find_date = list(map(getDate, date))

# 박스안에 날씨 부분 (맑음)이 속한 태그 불러오기
find_weather = data1.find_all('i', {'class' : 'ico _cnLazy'})

# 리스트 요소번호에 따라 홀수면 오전 날씨, 짝수면 오후 날씨를 나타냄
find_weather_icon = list(map(getIconNumber, find_weather))
AMlist=find_weather_icon[0::2]
PMlist=find_weather_icon[1::2]

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

if todayH < 12 :
    weatherli = []
    for i in range(0, 10):
        weather = result[i]['am']
        weatherli.extend(weather)
        intList = list(map(int, weatherli))
        print(intList)
    print(intList)

    for i in range(0, 10):
        Rweather = intList[i]
        if Rweather in sunny:
            sunnyImg.show()
        elif Rweather in cloud:
            cloudImg.show()
        elif Rweather in cloudRain:
            cloudRainImg.show()
        elif Rweather in cloudSunny:
            cloudSunnyImg.show()
        elif Rweather in rain:
            rainImg.show()
        elif Rweather in snow:
            snowImg.show()
        elif Rweather in sunnyRain:
            sunnyRainImg.show()
        else:
            thunderImg.show()

else :
    weatherli2 = []
    for i in range(0, 10):
        weather2 = result[i]['pm']
        weatherli2.extend(weather2)
        intList2 = list(map(int, weatherli2))
        print(intList2)
    print(intList2)

    for i in range(0, 10):
        Rweather2 = intList2[i]
        if Rweather2 in sunny:
            sunnyImg.show()
        elif Rweather2 in cloud:
            cloudImg.show()
        elif Rweather2 in cloudRain:
            cloudRainImg.show()
        elif Rweather2 in cloudSunny:
            cloudSunnyImg.show()
        elif Rweather2 in rain:
            rainImg.show()
        elif Rweather2 in snow:
            snowImg.show()
        elif Rweather2 in sunnyRain:
            sunnyRainImg.show()
        else:
            thunderImg.show()





# for item in find_weather:
#     weather = item.find('span').text
#     sunny = "맑음"
#     cloud = "구름"
#     cloudy = "흐림"
#     rain = "비"
#     fog = "안개"
#     if sunny in weather:
#         print("맑음")
#     elif cloud:
#         print("구름 많음")
#     elif cloudy:
#         print("흐림")
#     elif rain:
#         print("비")
#     elif fog:
#         print("안개")
#     else:
#         print("None")


# for item in find_weather:
#     print(item.find('span').text)




# # 이후에 온도정보도 추출해보자
# find_curr_temp = data1.find('span', {'class' : 'todaytemp'}).text
# print('현재 온도 : ' + find_curr_temp + '℃')
#
# # 미세먼지와, 초미세먼지, 오존지수는 각 줄이 dd라는 공통된 태그를 갖고 있다.
# # 클래스명이 지수에 따라 계속 변화한다. find 함수는 첫 정보만을 반환하므로 findAll함수를 이용
# data2 = data1.findAll('dd')
#
# # data2 에 저장된 dd 태그 코드들 안에있는 span, num 클래스를 추출하면 총 3개의 정보를 얻을 수 있음
# find_dust = data2[0].find('span', {'class' : 'num'}).text
# find_ultra_dust = data2[1].find('span', {'class' : 'num'}).text
# find_ozon = data2[2].find('span', {'class' : 'num'}).text
# print('현재 미세먼지 : ' + find_dust)
# print('현재 초미세먼지 : ' + find_ultra_dust)
# print('현재 오존지수 : ' + find_ozon)
from bs4 import BeautifulSoup
# pprint 는 딕셔너리의 데이터가 긴 경우에 좀 더 보기 편하게 도와준다.
from pprint import pprint
import requests
import numpy as np


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

# 박스안에 날씨 부분 (맑음)이 속한 태그 불러오기
find_weather = data1.find_all('i', {'class' : 'ico _cnLazy'})

find_weather_icon = list(map(getIconNumber, find_weather))
print(find_weather_icon)


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
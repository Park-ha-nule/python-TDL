from bs4 import BeautifulSoup
# pprint 는 딕셔너리의 데이터가 긴 경우에 좀 더 보기 편하게 도와준다.

import requests
import datetime

def getDate(date):
    return date.text

# 웹페이지 요청을 하는 코드. 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
html = requests.get('https://n.weather.naver.com/today/09140104')

# 파이썬에서 보기 좋게, 파싱 작업을 거쳐야 각 요소에 접근이 쉬워짐
# 이것을 도와주는게 beautifulSoup 이다.
soup = BeautifulSoup(html.text, 'html.parser')

# 주간예보를 먼저 불러옴 (중복되는 클래스가 있어서 전체로 안하고 주간예보로 먼저 짜르고 시작함)
weekly = soup.find('div', {'id' : 'weekly'})

# 주간 예보 안에 내가 필요한 일주일 날씨 박스만 불러옴
weatherbox = weekly.find('div', {'class':'scroll_area'})

date = weatherbox.find_all('span', {'class' : 'date'})
find_date = list(map(getDate, date))


# 날짜 불러오기
date = weatherbox.find_all('span', {'class' : 'date'})
find_date = list(map(getDate, date))

# split 을 씀으로써 /를 기준으로 나눠서 문자열을 배열로 만들어줌
def getTemp(temp):
    return temp.text.replace("최고기온", "").replace("최저기온", "").replace("°", "").split("/")

# 박스안에 온도 부분 가져오기
find_temp = weatherbox.find_all('strong', {'class' : 'temperature'})
temp_list = list(map(getTemp, find_temp))

def getAM(array):
    return array[0]
def getPM(array):
    return array[1]

# 가져온 온도 배열 중 원소 하나하나를 map 으로 돌린다고 생각 인덱스가 0인 경우와 1인 경우로 AM, PM을 나눔
AMlist = list(map(getAM, temp_list))
PMlist = list(map(getPM, temp_list))

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

success = [{
    "date" : find_date,
    "am" : AMlist,
    "pm" : PMlist
}]
print(success)


# if todayH < 12:
#     templi = []
#     for i in range(0, 10):
#         temp = result[i]['am']
#         templi.append(temp)
#         intList = list(map(int, templi))
#     print(intList)
# else:
#     templi2 = []
#     for i in range(0, 10):
#         temp = result[i]['pm']
#         templi2.append(temp)
#         intlist = list(map(int, templi2))
#     print(intlist)
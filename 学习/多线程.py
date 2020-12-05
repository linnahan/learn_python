import requests,threading
def get_weather(city):
    req=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)
    dic_city=req.json()
    city_data=dic_city.get('data')
    print(city_data.get('city'))
    if city_data:
        city_forecast=city_data['forecast'][0]
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
threads=[]
citys=['北京','上海','汕头','武汉','茂名']
files=range(len(citys))
for i in files:
    t=threading.Thread(target=get_weather,args=(citys[i],))
    threads.append(t)
for i in files:
    threads[i].start()
for i in files:
    threads[i].join()
print('结束获取')
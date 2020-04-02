import requests
while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print('查询失败')
        break
    dic_city=req.json()
    #print(dic_city)
    city_data=dic_city.get('data')
    #print(city_data)
    if city_data:
        city_forecast=city_data['forecast'][0]
        #print(city_forecast)
        print(city_forecast.get('type'))
        print(city_forecast.get('low'))
        print(city_forecast.get('high'))
        print(city_forecast.get('date'))
    else:
        print('未获得')
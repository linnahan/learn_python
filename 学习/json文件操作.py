import json

with open("info.json",encoding="utf-8") as f:
    buf = json.load(f)
    for info in buf:
        print(f"姓名：{info.get('name')} 年龄：{info.get('age')} 性别：{info.get('sex')} 城市：{info.get('adress').get('city')}")
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data2 = json.dumps(data)
print(data2)
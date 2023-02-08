import csv


def dect_to_csv():
    '''将python字典类型写入到csv文件'''
    data = [{"id":"1","name":"小美","sex":0},{"id":"2","name":"小","sex":1},{"id":"3","name":"美","sex":0}]
    with open(r"C:\Users\admin\Desktop\a.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id","name","sex"])
        writer.writeheader()
        writer.writerows(data)

def csv_to_dect():
    '''将csv文件加载为python字典'''
    with open(r"C:\Users\admin\Desktop\a.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:      # row可以当成字典用
            print(row)

dect_to_csv()
csv_to_dect()
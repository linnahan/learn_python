import csv
import random



# 生成随机手机号
import time


def get_r_phone(n = 1):
    head = ["152","137","136","135","156","186"]
    phone_list = []
    for i in range(n):
        phone = random.choice(head) + "%08d"%random.randrange(0,99999999)
        phone_list.append(phone)
    if n == 1:
        return phone_list[0]
    return phone_list

# pymysql二次封装，方便使用
class Easymysql():
    def __init__(self,db):
        self.db = db
        self.cursor = db.cursor()
    def create_table(self,tablename,encoding="utf8",**para):
        self.tablename = tablename
        self.head = [x for x in para.keys()]
        indata_list = []
        for key in self.head:
            indata_list.append(f"{key} {para[key]} ,")
        indata = "".join(indata_list)
        charset = f"ENGINE=InnoDB DEFAULT CHARSET={encoding};"
        table = f'''create table {tablename} (
                    id int NOT NULL AUTO_INCREMENT,
                    {indata}
                    PRIMARY KEY (id)) {charset}'''
        try:
            self.cursor.execute(table)
        except Exception as f:
            print(f)
            self.db.rollback()
        finally:
            return self
    def _writemanydict(self, table, manydata):
        for data in manydata:
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values})' \
                .format(table=table, keys=keys, values=values)
            try:
                self.cursor.execute(sql, tuple(data.values()))
            except Exception as f:
                print(f)
                self.db.rollback()
                return
        self.db.commit()
    def writemany(self, table, manydata):  # [{},{},{}]or[[],[],[]]or csv.DictReader
        if isinstance(manydata, csv.DictReader):
            self._writemanydict(table,manydata)
        elif isinstance(manydata[0] , dict):
            self._writemanydict(table, manydata)
        elif isinstance(manydata[0], list):    # [[],[],[]]
            headdata = manydata[0]
            keys = ", ".join(headdata)
            bodydata = manydata[1:]
            for data in bodydata:   # []
                values = ", ".join(['%s' * len(data)])
                sql = 'INSERT INTO {table}({keys}) VALUES ({values})' \
                    .format(table=table, keys=keys, values=values)
                try:
                    self.cursor.execute(sql, list(data))
                except Exception as f:
                    print(f)
                    self.db.rollback()
                    return
            self.db.commit()
        else:
            print("请把manydata规范为[{},{},{}]or[[],[],[]]or csv.DictReader生成器")
    def execute(self, yg):
        return self.cursor.execute(yg)
    def fetchmany(self, n):
        return self.cursor.fetchmany(n)





if __name__ == '__main__':
    print(get_r_phone())

class House:
    def __init__(self,h_type,total_area):
        self.h_type = h_type
        self.total_area = total_area
        self.free_area = total_area
        self.item = []
    def __str__(self):
        return f"户型：{self.h_type} 总面积：{self.total_area} 剩余面积：{self.free_area} 家具名称：{self.item}"
    def add_item(self,*item):
        for i in item:
            self.free_area -= i.area
            self.item.append(i.name)

class HouseItem:
    def __init__(item,name,area):
        item.name = name
        item.area = area

house = House("别墅",20)
bed = HouseItem("bed",4)
chest = HouseItem("chest",2)
table = HouseItem("table",1.5)


house.add_item(bed,chest,table)
print(house)


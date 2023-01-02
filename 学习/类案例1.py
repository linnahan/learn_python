class House:
    def __init__(self,h_type,total_area):
        self.h_type = h_type
        self.total_area = total_area
        self.free_area = total_area
        self.item = []
    def __str__(self):
        return f"户型：{self.h_type} 总面积：{self.total_area} 剩余面积：{self.free_area} 家具名称：{self.item}"
    def add_item(self,item):
        if self.free_area > item.area:
            print(f"添加家具{item.name}成功")
            self.free_area -= item.area
            self.item.append(item.name)
        else:
            print("面积不足")

class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

if __name__ == '__main__':
    house = House("别墅",20)
    bed = HouseItem("席梦思",4)
    chest = HouseItem("衣柜",2)
    table = HouseItem("餐桌",1.5)
    bigbed = HouseItem("大大大", 18)

    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)
    house.add_item(bigbed)
    print(house)


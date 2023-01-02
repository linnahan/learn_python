# 定义一个电脑类(computer),
# 电脑有品牌(brand),有价格(price),能播放电影(play_movie)。
# 分别创建2个对象"小米电脑 `mi`" 和 "苹果电脑 `mac`"。分别调用放电影的动作,
# 输出内容格式如下: `xx 播放电影 oo`, xx 为 电脑品牌, oo 为电脑的名字, 电影名字作为参数传递即可
# - 小米电脑播放 `葫芦娃`
# - 苹果电脑 播放 `变形金刚`
class Computer:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def play_movie(self,movie):
        print(f"{self.brand} 播放电影 {movie}")
if __name__ == '__main__':
    mi = Computer("小米电脑",5000)
    mac = Computer("苹果电脑",8000)
    mi.play_movie("葫芦娃")
    mac.play_movie("变形金刚")


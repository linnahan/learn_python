import random
class Game:
    top_score = 0
    def __init__(self,player_name):
        self.play_name = player_name
    @staticmethod
    def show_help():
        print("开始游戏即可获得随机分数")
    @classmethod
    def show_top_score(cls):
        print(f"历史最高分：{cls.top_score}")
    def start_game(self):
        score = random.randint(1,100)
        print(f"开始游戏,玩家{self.play_name}本次分数为{score}")
        if score > Game.top_score:
            Game.top_score = score
if __name__ == '__main__':
    Game.show_help()
    a = Game("nahan")
    a.show_help()
    print(Game.top_score)
    a.start_game()
    a.start_game()
    print(Game.top_score)

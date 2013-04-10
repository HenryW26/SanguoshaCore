# how to use this core pack?

# core
class Game:
    """docstring for Game"""
    def __init__(self):
        pass
        # game init

    # 游戏开始
    def init(self):
        # 洗牌

        # 分配身份
        self._players = [Player(i+1) for i in range(self.player_count)]

        i = 0
        for id_type in self._id_types:
            for z in range(self._id_types[id_type]):
                self._players[i].type = id_type
                i = i + 1

        # 随机位置

    # 设置每种角色的数量
    def id_types(self, id_types):
        self._id_types = id_types

    # 获得某个角色
    def player(self, i):
        return self._players[i]

    # 获得所有角色
    def players(self, id_type):
        if id_type == 'other':
            return [p for p in self._players if p.type != 'king']
        return [p for p in self._players if p.type == id_type]

    # 选将
    def make_roles(self, player):
        if player.type == 'king':
            player.available_roles = [Role('sunquan') for i in range(5)]
        else:
            player.available_roles = [Role('guanyu') for i in range(3)]
        return player.available_roles

    
    def start(self):
        pass
        # 身份
        # 选将
        # 选将
        # 指定出牌人
    def current_player(self):
        return self.current_player

    # 返回游戏结果 胜利方
    def result():
        pass

def game_play():
    while true:
        for player in player_list:
            player.action()


class Player:
    """docstring for Player"""
    def __init__(self, index):
        self.index = index
    def action(self):
        pass
    def select_role(self, index):
        self.role = self.available_roles[index]

class Role:
    """docstring for Role"""
    def __init__(self, name):
        self.name = name
        
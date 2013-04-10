# how to use this core pack?

# core
class Game:
    """docstring for Game"""
    def __init__(self):
        # 回合内步骤
        self.mo       = 1 # 摸牌之前
        self.panding  = 2 # 判定闪电、乐不思蜀
        self.panding1 = 3 # 
        self.mo1      = 4 # 
        self.chupai   = 5 # 出牌阶段
        sefl.after    = 6 # 出牌结束

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

    # 开始游戏
    def start(self, first_player):
        self.round_player = first_player # 当前回合是属于哪个玩家的
        self.is_end = False
        self.step = 'mo' # 游戏步骤
        self.go_step()

    # 走一步 每当状态改变，就会自动停止
    # 然后等待调用者再次调用此方法
    def go_step(self):
        # 回合内步骤
        {
            'mo':       lambda: self.mo,       # 摸牌之前
            'panding':  lambda: self.panding,  # 判定闪电、乐不思蜀
            'panding1': lambda: self.panding1, # 
            'mo1':      lambda: self.mo1,      # 
            'chupai':   lambda: self.chupai,   # 出牌阶段
            'after':    lambda: sefl.after    # 出牌结束
        }[self.step]();

    def status(self):
        return {'step': self.step}

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

    # 根据用户输入行动
    def act(self, react):
        pass
    def select_role(self, index):
        self.role = self.available_roles[index]

class Role:
    """docstring for Role"""
    def __init__(self, name):
        self.name = name
        
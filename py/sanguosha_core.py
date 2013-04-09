# how to use this core pack?


# core
class Game:
    """docstring for Game"""
    def __init__(self):
        pass
        # game init
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
    def id_types(self, id_types):
        self._id_types = id_types
    def player(self, i):
        return self._players[i]
    
    def king_roles(self):
        id_type = 'king'
        return {"player": self.players(id_type)[0], "roles": self.make_roles(id_type)}
    def players(self, id_type):
        return [p for p in self._players if p.type == id_type]
    def make_roles(self, id_type):
        if id_type == 'king':
            return {'player': self._players[0], 'roles': [Role('zhenji') for i in range(5)]}
        return [Role('zhe') for i in range(3)]
    def start(self):
        pass
        # 身份
        # 选将
        # 选将
        # 指定出牌人
    def current_player(self):
        return self.current_player

def game_play():
    while true:
        for player in player_list:
            player.action()

def game_end():
    return get_win()

class Player:
    """docstring for Player"""
    def __init__(self, index):
        self.index = index
    def action(self):
        pass

class Role:
    """docstring for Role"""
    def __init__(self, name):
        self.name = name
        
            
# test    
if __name__ == '__main__':
    def show_game_roles(pr):
        pass
    def get_user_input_role_select():
        return 1

    game = Game()
    game.player_count = 5
    game.id_types({'king': 1, 'loyal': 1, 'sinister': 1, 'rebel': 2})

    game.init() # 洗牌 分配身份

    # 主公选将
    king = game.players('king')
    roles = game.select_roles(king)
    print(roles)
    show_game_roles(roles)

    role_id = get_user_input_role_select()
    print(role_id)
    king.role_selector = role_id

    # 其他人选将
    players = game.players('other')
    while player:
        show_game_roles(player)
        role_id = get_user_input_role_select()
        player.player.role_selector = role_id

    # game.start(king.player) # 从主公开始出牌

    # while not game.is_end():
    #     player = game.current_player()
    #     while true:
    #         react = get_user_input_react()
    #         show_game_status(game.status())
    #         if player.act(react):
    #             game.go_step()
    #             break

    # # 游戏结束，显示结果
    # result = game_end()
    # show_game_result(result)

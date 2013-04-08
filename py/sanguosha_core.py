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
        

        # 随机位置
    def king_roles(self):
        id_type = 'king'
        return {"player": self.players(id_type)[0], "roles": self.make_roles(id_type)}
    def players(self, id_type):
        return [p for p in self._players if p.type == id_type]
             
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
    def __init__(self, n):
        self.n = n
    def action(self):
        pass
            
# test    
if __name__ == '__main__':
    def show_game_roles(pr):
        pass
    def get_user_input_role_select():
        return 1

    game = Game()
    game.player_count = 5
    game.king_count = 1
    game.loyal_count = 1
    game.cheat_count = 1
    game.rebel_count = 2

    game.init() # 洗牌 分配身份

    # 主公选将
    king = game.king_roles() # return king player and roles
    show_game_roles(king)
    role_id = get_user_input_role_select()
    king.player.role_selector = role_id

    # # 其他人选将
    # player = game.player_roles()
    # while player:
    #     show_game_roles(player)
    #     role_id = get_user_input_role_select()
    #     player.player.role_selector = role_id

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

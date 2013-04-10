# show how to use this core pack
# 一个简易的控制台版的三国杀

from sanguosha_core import *

def show_game_roles(player, roles):
    print('player', player.index, player.type)
    print('请在以下角色中选择')
    for r in roles:
        print(r.name)
def get_user_input_role_select():
    return 1

game = Game()
game.player_count = 5
game.id_types({'king': 1, 'loyal': 1, 'sinister': 1, 'rebel': 2})

game.init() # 洗牌 分配身份

# 主公选将
king = game.players('king')[0]
roles = game.make_roles(king)
show_game_roles(king, roles)

role_id = get_user_input_role_select()

king.select_role(role_id)

# 其他人选将
players = game.players('other')
for p in players:
    roles = game.make_roles(p)
    show_game_roles(p, roles)
    role_id = get_user_input_role_select()
    p.select_role(role_id)

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
# result = game.result()
# show_game_result(result)

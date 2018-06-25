card = [None, None, None, "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
# プレイヤーと順位をインデックス値で管理
players = input().split(" ")
ranking = {i: 0 for i in range(len(players))}
# ranking = {}
# for i in range(len(players)):
#     ranking[i] = 0
count = 0
rankN = 1
turnN = 0  # ターン数、プレイヤーのインデックス値。２つの役割がある為ややこしい
PLPut = 0  # Player who Last Put 最後にカードを置いたプレイヤーのインデックス値。いい変数名が思いつかない
nowCard = 0
# player_is_in = True
def strongest(players):
  return max([card.index(player) for player in players if player],key=int)
# inPlayers = lambda lists: any(lists)
# def inPlayers(lists):  # すべてのプレイヤーが None かチェック
#     for i in lists:
#         if i is not None:
#             return True
#     return False

while rankN < 53:  # プレイヤーがすべて None になるまで実行
    count += 1
# while player_is_in:  # プレイヤーがすべて None になるまで実行
    if turnN >= len(players):  # ターン数がプレイヤーの総数を超えたらリセット
        turnN = 0
    if PLPut == turnN:  # 最後にカードを置いたプレイヤーにターンが来たら場のカードを初期化
        nowCard = 0

    pCard = card.index(players[turnN])  # card のインデックス値でカードの強さを決める
    if pCard is not None and pCard > nowCard:  # 場のカードより強いときの処理
    # if pCard is not None and pCard > nowCard or strongest(players) == pCard:  # 場のカードより強いときの処理
        ranking[turnN] = rankN
        rankN += 1
        nowCard = pCard
        PLPut = turnN
        players[turnN] = None

    # player_is_in = inPlayers(players)
    turnN += 1

# print("\n".join([str(i) for i in ranking.values()]))
# for i in ranking.values():
#     print(i)
    print(count)
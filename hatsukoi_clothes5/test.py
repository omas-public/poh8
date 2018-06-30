# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes5

def player_ranking(card_list):
  from itertools import cycle

  # Define Function
  pluck = lambda table: lambda key: table[key]
  convert = pluck(dict(zip(list(map(str,range(3, 11))) + list('JQKA2'), list(range(13)))))
  is_win = lambda player, dealer: player['card'] > dealer['card']
  is_strongest = lambda dealer, players: dealer['card'] >= max([p['card'] for p in players if p['rank'] == None])

  # Declair Variable
  players = [{'card':convert(card), 'rank': None} for card in card_list] # cardを強さに応じた数値に変換
  num_player = len(players)        # プレイヤー数　
  index = cycle(range(num_player)) # [0, 1, 2, ...num_player -1, 0, 1, 2, ...]  繰り返しのイテレータ
  rank  = 1                        # 順位

  dealer = players[next(index)]    # 最初の親
  dealer['rank'] = rank            # 最初の親は1位

  while rank < num_player:
    player = players[next(index)]  # イテレータを使って次のカードを取り出す

    # ランクが決まっていなくかつディーラーに勝つか，またはディーラーが最強のカードなら
    if not player['rank'] and (is_win(player, dealer) or is_strongest(dealer, players)):
      rank += 1
      player['rank'] = rank
      dealer = player   #

  return [player['rank'] for player in players]

def display(players):
  print('\n'.join(map(str,players)))

if __name__ == '__main__':

  card_list  = input().split(' ')
  display(player_ranking(card_list))

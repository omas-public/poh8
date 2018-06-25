# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes5
def func1():
  # Define Function
  next  = lambda n: n % 52
  isWin = lambda x, y: x > y


  # Declair Variable

  strength = dict(zip(
    list(map(str,range(3, 11))) + list('JQKA2')
    , list(range(1, 14))))

  card_list  = [card for card in [strength[s] for s in input().split(' ')]]
  num_player = len(deck)
  rank_list  = [None] * num_player

  player_index = 0
  pass_index   = 0

  rank         = 0


  while rank < num_player:
    index = next(index)
    if rank_list[player_index] != None: continue

    player = card_list[player_index]
    if isWin(player, dealer) or pass_index == num_player:
      rank_list[rank] = player_index
      rank += 1
      pass_index = 0
    else:
      pass_index += 1


def func3(card_list):
  print(card_list)


if __name__ == '__main__':
  strength = dict(zip(
    list(map(str,range(3, 11))) + list('JQKA2')
    , list(range(13))))
  card_list  = [strength[s] for s in input().split(' ')]

  func3(card_list)

# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye3
def func1(p):
  bp = p // 100
  if p >= 1000:
    bp += 10
  print(bp)

def func2(p):
  return p // 100 + 10 if p >= 1000 else 0

def func3(p):
  return p // 100 + ((0), (10))[p >= 1000]

def func4(p):
  bp1 = lambda p: p // 100
  bp2 = lambda p: ((0), (10))[p >= 1000]
  get_bonus = lambda p: bp1 + bp2
  return get_bonus(p)

def display(n):
  print(n)

if __name__ == '__main__':
  p = int(input())
  display(func4(p))

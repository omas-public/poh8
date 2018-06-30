# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair2
def func1(n, s):
  # loopを使ってPrint
  count = 0
  while count < int(n):
    print(s)
    count += 1

def func2(n, s):
  # loopを使ってPrint
  for _ in range(int(n)):
    print(s)

def func3():
  # 文字を掛け算して、最後の改行を抑制
  print((s + '\n') * int(n), end = '')

def func4(n, s):
  # listを作る
  return [s for _ in range(int(n))]


def func5(n, s):
  # listを掛け算
  return [s] * int(n)

def display(l):
  print('\n'.join(l))

if __name__ == '__main__':
  n, s = [input() for _ in range(2)]
  display(func5(n, s))

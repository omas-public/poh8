# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair2
def func1():
  # loopを使ってPrint  
  n, s = [input() for _ in range(2)]
  count = 0
  while count < int(n):
    print(s)
    count += 1

def func2():
  # loopを使ってPrint
  n, s = [input() for _ in range(2)]
  for _ in range(int(n)):
    print(s)

def func3():
  # listを作って、改行を間に挟んでPrint
  n, s = [input() for _ in range(2)]
  l = [s for _ in range(int(n))]
  print('\n'.join(l))

def func4():
  # listを掛け算して、改行を間に挟んでPrint
  n, s = [input() for _ in range(2)]
  print('\n'.join([s] * int(n)))

def func5():
  # 文字を掛け算して、最後の改行を抑制
  n, s = [input() for _ in range(2)]
  #print((s + '\n') * int(n), end='')


if __name__ == '__main__':
  func1()
  #func2()
  #func3()
  #func4()
  #func5()
# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair3
def func1():
  n = int(input())
  if n % 7 == 0:
    print('lucky')
  else:
    print('unlucky')

def func2():
  n = int(input())
  prefix = 'un' if n % 7 != 0 else ''
  print(prefix + 'lucky')

def func3():
  n = int(input())
  print('lucky' if n % 7 == 0 else 'unlucky')

def func4():
  n = int(input())
  print(('un' if n % 7 else '') + 'lucky')

def func5():
  n = int(input())
  print((('un'),(''))[n % 7] + 'lucky')

if __name__ == '__main__':
  # func1()
  # func2()
  # func3()
  func4()
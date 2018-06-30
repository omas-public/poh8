# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes2
def func1(n, m):
  if m % n == 0:
    print('ok')
  else:
    print('ng')

def func2(n, m):
  print('ok' if m % n == 0 else 'ng')

def func3():
  return 'ng' if m % n else 'ok'

def func4():
  from numpy import mod
  message = lambda pred: (('ng'), ('ok'))[pred]
  return message(mod(m, n) == 0)

def display(s):
  print(s)

if __name__ == '__main__':
  n, m = map(int, input().split(' '))
  display(func4(n, m))
# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes2
def func1():
  n, m = map(int, input().split(' '))
  if m % n == 0:
    print('ok')
  else:
    print('ng')

def func2():
  n, m = map(int, input().split(' '))
  print('ok' if m % n == 0 else 'ng')

def func3():
  n, m = map(int, input().split(' '))
  print('ng' if m % n else 'ok')

def func4():
  from numpy import mod
  message = lambda pred: (('ng'), ('ok'))[pred] 
  n, m = map(int, input().split(' '))
  print(message(mod(m, n) == 0))

if __name__ == '__main__':
  func4()
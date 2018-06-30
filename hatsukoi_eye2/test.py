# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye2
def func1(s, n):
  if s >= n:
    print('OK')
  else :
    print('NG')

def func2(s, n):
  print('OK' if s >= n else 'NG')

def func3(s, n):
  print((('NG'),('OK'))[s >= n])

def func4(s, n):
  message = lambda pred: (('NG'),('OK'))[pred]
  return message(s >= n)

if __name__ == '__main__':
  s, n = map(int, input().split())


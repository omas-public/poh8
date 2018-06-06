# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye2
def func1():
  s, n = map(int, input().split())
  if s >= n:
    print('OK')
  else :
    print('NG')
  
def func2():
  s, n = map(int, input().split())
  print('OK' if s >= n else 'NG')

def func3():
  s, n = map(int, input().split())
  print((("NG"),("OK"))[s >= n])  

def func4():
  message = lambda pred: (("NG"),("OK"))[pred]
  s, n = map(int, input().split())
  print(message(s >= n))

if __name__ == '__main__':
  func1()

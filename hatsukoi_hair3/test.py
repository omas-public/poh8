# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair3
def func1(n):
  if n % 7 == 0:
    print('lucky')
  else:
    print('unlucky')

def func2(n):
  return 'lucky' if n % 7 == 0 else 'unlucky'

def func3(n):
  prefix = 'un' if n % 7 != 0 else ''
  return prefix + 'lucky'

def func4(n):
  return ('un' if n % 7 else '') + 'lucky'

def func5(cond):
  s = 'unlucky'
  return s.replace('un', '') if cond else s

def func6(cond):
  return '{neg_prefix}lucky'.format(neg_prefix=(('un'),(''))[cond])


def display(s):
  print(s)

if __name__ == '__main__':
  n = int(input())
  display(func5(n % 7))
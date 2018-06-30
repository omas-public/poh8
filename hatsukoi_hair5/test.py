# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair5
def func1(s, t):
  for i in range(s):
    if i == t - 1:
     print('+', end='')
    else:
     print('-', end='')

def func2(s, t):
  prefix = '-' * (t - 1)
  suffix = '-' * (s - t)
  print('{}+{}'.format(prefix, suffix))

def func3(s, t):
  s, t = [int(input()) for _ in range(2)]
  line = s * '-'
  print('{}+{}'.format(line[:t - 1], line[t:]))

def func4(s, t):
  array = ['-'] * s
  array[t - 1] = '+'
  return array

def display(array):
  print(''.join(array))

if __name__ == '__main__':
  s, t = [int(input()) for _ in range(2)]
  display(func4(s, t))

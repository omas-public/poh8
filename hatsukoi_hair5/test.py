def func1():
  s, t = [int(input()) for _ in range(2)]
  for i in range(s):
    if i == t - 1:
      print('+', end='')
    else:
      print('-', end='')

def func2():
  s, t = [int(input()) for _ in range(2)]
  prefix = '-' * (t - 1)
  suffix = '-' * (s - t)
  print('{}+{}'.format(prefix, suffix))

def func3():
  s, t = [int(input()) for _ in range(2)]
  line = s * '-'
  print('{}+{}'.format(line[:t - 1], line[t:]))

def func4():
  s, t = [int(input()) for _ in range(2)]
  array = [s] * '-'
  array[t - 1] = '+'
  print(''.join(array))
  
def func5():


if __name__ == '__main__':

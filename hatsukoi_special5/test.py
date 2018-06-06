# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special5
def func1():
  n, m = [int(input()) for _ in range(2)]

  week_event = n * 2
  count = 0
  while (m > 0):
    m -= week_event
    count += 1
  
  print(count)

def func2():
  n, m = [int(input()) for _ in range(2)]
  week_event = n * 2
  if (m / week_event > m // week_event):
    print((m // week_event) + 1)
  else:
    print(m // week_event)

def func3():
  from math import ceil
  n, m = [int(input()) for _ in range(2)]
  week_event = n * 2
  print(ceil(m / week_event))

if __name__ == '__main__':
  func1()

# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special6

def func1(n, p, m, q):
  paper = p * n
  pen   = q * (n + (m - 1)) // m
  print(paper + pen)

def func2(n, p, m, q):
  from math import ceil
  return  sum([p * n, q * ceil(n / m)])

def display(n):
  print(n)

if __name__ == '__main__':
  [[n, p], [m, q]] = [map(int, input().split(' ')) for _ in range(2)]
  display(func2(n, p, m, q))

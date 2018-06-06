# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special6
def func1():
  n, p = map(int, input().split(' '))
  m, q = map(int, input().split(' '))

  paper = p * n
  pen   = q * (n + (m - 1)) // b
  print(paper + pen)

def func2():
  from math import ceil
  n, p = map(int, input().split(' '))
  m, q = map(int, input().split(' '))

  print(sum([p * n, q * ceil(n / m)]))  

if __name__ == '__main__':
  func1()

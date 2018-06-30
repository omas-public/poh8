# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_eye4
def func1(N, alist):
  for i in range(N - 1, 0, -1):
    for j in range(i):
      if alist[j] > alist[j + 1]:
        tmp = alist[j + 1]
        alist[j + 1] = alist[j]
        alist[j] = tmp
  return  alist[N // 2]


def func2(N, alist):
  for i in range(N - 1, 0, -1):
    for j in range(i):
      if alist[j] > alist[j + 1]:
        alist[j + 1], alist[j] = alist[j], alist[j + 1]
  return alist[N // 2]

def func3(N, alist):
  alist.sort()
  return(alist[N // 2])

def func4(N, alist):
  return sorted(alist)[N // 2]

def func5(alist):
  from statistics import median
  return median(alist)

def display(n):
  print(n)


if __name__ == '__main__':
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  display(func5(alist))
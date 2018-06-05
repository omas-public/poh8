def func1():
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  
  for i in range(N - 1, 0, -1):
    for j in range(i):
      if alist[j] > alist[j + 1]:
        tmp = alist[j + 1]
        alist[j + 1] = alist[j]
        alist[j] = tmp

def func2():
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  
  for i in range(N - 1, 0, -1):
    for j in range(i):
      if alist[j] > alist[j + 1]:
        alist[j + 1], alist[j] = alist[j], alist[j + 1]

  print(alist[N // 2])

def func3():
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  
  alist.sort()
  print(alist[N // 2])

def func4():
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  
  print(sorted(alist)[N // 2])

def func5():
  from statistics import median
  N = int(input())
  alist = list(map(int, input().split(' ')))[:N]
  print(median(alist))

if __name__ == '__main__':
  func5()

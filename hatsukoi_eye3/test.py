def func1():
  p = int(input())
  bp = p // 100
  if p >= 1000:
    bp += 10
  print(bp)

def func2():
  p = int(input())
  print(p // 100 + 10 if p >= 1000 else 0)

def func3():
  p = int(input())
  print(p // 100 + ((0), (10))[p >= 1000])

def func4():
  bp1 = lambda p: p // 100
  bp2 = lambda p: ((0), (10))[p >= 1000]
  get_bonus = lambda p: bp1 + bp2
  p = int(input())
  print(get_bonus(p))



if __name__ == '__main__':
  func1()

# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair4
def func1(des):
  count = 0

  for [d, e] in des:
    if d == e:
      count += 1

  if count >= 3:
    print('OK')
  else:
    print('NG')

def func2(des):
  count = 0
  for d,e in des:
    if d == e:
      count += 1

  return 'OK' if count >= 3 else 'NG'

def func3(des):
  is_same = lambda d, e: d == e
  count = len([[d, e] for d, e in des if is_same(d, e)])

  return 'OK' if count >= 3 else 'NG'

def display(s):
  print(s)

if __name__ == '__main__':
  des = [input().split(' ') for _ in range(5)]

  display(func3(des))
def func1():
  count = 0

  for [d, e] in [input().split(' ') for _ in range(5)]:
    if d == e:
      count += 1

  if count >= 3:
    print('OK')
  else:
    print('NG')

def func2():
  des = [input().split(' ') for _ in range(5)]
  count = 0
  for d,e in des:
    if d == e:
      count += 1
  
  print('OK' if count >= 3 else 'NG')

def func3():
  is_same = lambda de: de[0] == de[1]
  count = len(list(filter(is_same, [input().split(' ') for _ in range(5)])))
  
  print('OK' if count >= 3 else 'NG')

if __name__ == '__main__':
  func3()
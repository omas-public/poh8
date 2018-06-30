# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_special2
def func1(s, t):

  for c in s:
    if c in t:
      t = t.replace(c,'', 1)

  print(len(t))

def func2(s, t):

  uniq = set(t)
  count = 0

  for c in uniq:
    diff = len(t.split(c)) - len(s.split(c))
    count += (diff if diff > 0 else 0)

  print(count)

def func3(s, t):

  print(sum(filter(lambda v: v > 0
    , [len(t.split(c)) - len(s.split(c)) for c in set(t)])))

def func4(s, t):
  def count_char(word):
    dic = {}
    for c in word:
      if c in dic:
        dic[c] += 1
      else:
        dic[c] = 1
    return dic

  sdic = count_char(s)
  tdic = count_char(t)

  count = 0
  for key in tdic:
    if not key in sdic:
      count += tdic[key]
    else:
      if tdic[key] > sdic[key]:
        count += (tdic[key] - sdic[key])

  return count

def func5(s, t):
  from collections import Counter

  sdic = Counter(s)
  tdic = Counter(t)
  count = 0
  for k, v in tdic.items():
    if k not in sdic:
      count += k
    if k in sdic and v > sdic[k]:
      count += v - sdic[k]

  return count

def func6(s, t):
  from collections import Counter
  return sum((Counter(t) - Counter(s)).values())

def display(n):
  print(n)

if __name__ == '__main__':
  n, m = map(int, input().split(' '))
  s, t = [input() for _ in range(2)]
  display(func6(s, t))

# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_hair6
# for と ifを使った普通のパターン
def func1(n, m, ts):

  remain_sec = n * 60
  music_count= 0

  for t in ts:
    if t < remain_sec:
      print(music_count ,t, remain_sec)
      remain_sec -= t
      music_count += 1
    else:
      break

  if music_count == m:
    print('OK')
  else:
    print(music_count)

def func2(n, m, ts):

  remain_sec = n * 60
  music_count= 0
  index = 0
  while (index < len(ts)):
    if remain_sec >= ts[index]:
      remain_sec -= ts[index]
      music_count += 1
      index += 1
    else:
      break

  print((str((music_count)),('OK'))[music_count == m])

def func3(n, m, ts):
  class Sec:
    def __init__(self, time):
      self.time = time
    def update(self, t):
      self.time -= t
      return self.time >= 0

  remain_sec = Sec(n * 60)
  music_count = len(list(filter(remain_sec.update, ts)))
  return ((str(music_count)),('OK'))[music_count == m]


def func4(n, m, ts):
  def is_enough(rest):
    def inner(sec):
        nonlocal rest
        rest -= sec
        return rest >= 0
    return inner

  music_count = len(list(filter(is_enough(n * 60), ts)))
  return ((str(music_count)),('OK'))[music_count == m]

def func5(n, m, ts):
  def gen(rest, list):
    for time in list:
      if rest >= time:
        rest -= time
      yield rest >= 0

  music_count = len(list(gen(n * 60, ts)))
  return ((music_count),('OK'))[music_count == m]

def display(s):
  print(s)

if __name__ == '__main__':
  n, m = [int(input()) for _ in range(2)]
  ts   = [int(input()) for _ in range(m)]

  display(func5(n, m, ts))

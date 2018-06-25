# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes6

def test1():
  N = int(input())
  log = dict([input().split(' ') for _ in range(N)])
  acc_temp = 0
  acc_cost = 0
  for i in range(24):
    acc_temp = max(acc_temp - 1, 0)
    if str(i) in log:
      acc_temp += {'out': 3, 'in': 5}[log[str(i)]]

    acc_cost += [1, 2][acc_temp != 0]

  print(acc_cost)

def test2():

  def thermometor(action_table, default = 0):
    cool = lambda x : x - 1 if x != 0 else 0
    temp = default
    def exec(action):
      nonlocal temp
      temp = cool(temp)
      temp += action_table[action]
      return temp
    return exec

  calc_cost = lambda temp: 1 if temp == 0 else 2

  N = int(input())
  logs    = dict([input().split(' ') for _ in range(N)])
  actions = [logs[str(i)] if str(i) in logs else 'none' for i in range(24)]

  print(sum(map(calc_cost
            ,(map(thermometor({'none':0, 'out': 3, 'in': 5}), actions)))))

def test3():
  def thermometor(default = 0):
    temp = default
    def exec(degrees):
      nonlocal temp
      temp = max(temp - 1, 0)
      temp += degrees
      return temp
    return exec

  calc_cost = lambda temp: 1 if temp == 0 else 2

  N = int(input())
  log = dict([input().split(' ') for _ in range(N)])
  temp_log = [{'out': 3, 'in': 5}[log[str(i)]]
                if str(i) in log else v for i, v in enumerate([0] * 24)]

  print(sum(map(calc_cost, map(thermometor(), temp_log))))

def test4():
  from functools import reduce
  def refrigerator():
    temp = 0
    def exec(cost, degrees):
      nonlocal temp
      temp = max(temp - 1, 0)
      temp += degrees
      cost += [1, 2][temp != 0]
      return cost
    return exec


  N = int(input())
  log = dict([input().split(' ') for _ in range(N)])
  cost = reduce(refrigerator(),[{'out': 3, 'in': 5}[log[str(i)]]
                if str(i) in log else v for i, v in enumerate([0] * 24)], 0)
  print(cost)



if __name__ == '__main__':
  test4()
# https://paiza.jp/poh/hatsukoi/challenge/hatsukoi_clothes3
def func1(M, N):
  if M >= N:
    print(M - N)
  else:
    print(0)

def func2(M, N):
  print(0 if N > M else M - N)

def func3(M, N):
  message = lambda m, n: ((m - n),(0))[n > m]
  return message(M, N)

def display(n):
  print(n)

if __name__ == '__main__':
  M, N = map(int, input().split(' '))
  display(func3(M, N))
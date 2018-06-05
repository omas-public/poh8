def func1():
  M, N = map(int, input().split(' '))
  if M >= N:
    print(M - N)
  else:
    print(0)

def func2():
  M, N = map(int, input().split(' '))
  print(0 if N > M else M - N)

def func3()
  message = lambda m, n: ((m - n)(0))[n > m]
  M, N = map(int, input().split(' '))
  print(message(M, N))

if __name__ == '__main__':
  func1()
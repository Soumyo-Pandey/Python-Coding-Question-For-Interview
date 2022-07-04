t = int(input())
for _ in range(t):
  X, Y = map(int,input().split())
  if X < Y:
    print('0')
  else:
    print('X - Y')

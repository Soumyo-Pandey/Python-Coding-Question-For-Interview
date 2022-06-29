n = int(input())
for i in range(n):
  x,y=map(int,input().split())
  if x>y:
    print(7 - x)
  else:
    print(7 - y)

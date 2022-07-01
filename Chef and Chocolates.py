#Chef and Chocolates

u = int(input())
for i in range(u):
  x,y,z=map(int,input().split())
  print((x*5+y*10)//z)

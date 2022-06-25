#Print the unique item form the list

n = int(input())
a = [0]*n
for i in range(n):
  a[i] = int(input())

for i in a:
  if a.count(i)==1:
    print(i)
    break
else:
  print(-1)

t = int(input())
odd = []
eve = []
for i in range(t):
  k = int(input())
  if k%2 == 0:
    eve.append(k)
  else:
    odd.append(k)
eve.sort()
odd.sort()
print(odd,eve)

##Count the Acs

for i in range(int(input())):
  y=int(input())
  if(y%100//100<=10):
    print(y//100+y%100)
  else:
    print("-1")

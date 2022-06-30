a = int(input())
b = []
for _ in range(a):
    b.append(input())

cab = []
for i in b:
    y=i.split('-')
    temp = "-".join(y[::-1])
    cab.append(temp)
cab.sort()
for i in cab:
    y=i.split('-')
    temp = "-".join(y[::-1])
    print(temp)
    

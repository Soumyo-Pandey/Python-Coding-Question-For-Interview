## Find the number of Cells in Excel Sheet.
Que="A10:C8"
p=Que.split(":")

a=p[0][0]
b=p[1][0]

c=p[0][1:]
d=p[1][1:]

if (a == b and c == d):
    print("Invalid")
else:
    m = abs(int(c)-int(d))+1
    n = abs(ord(a)-ord(b))+1
print(m*n)


## Second Code

Que="B10:F20"
p=Que.split(":")

a=p[0][0]
b=p[1][0]

c=p[0][1:]
d=p[1][1:]

if (a == b and c == d):
    print("Invalid")
else:
    m = abs(int(c)-int(d))+1
    n = abs(ord(a)-ord(b))+1
print(m*n)

##Third Program

Que="A1:A2"
p=Que.split(":")

a=p[0][0]
b=p[1][0]

c=p[0][1:]
d=p[1][1:]

if (a == b and c == d):
    print("Invalid")
else:
    m = abs(int(c)-int(d))+1
    n = abs(ord(a)-ord(b))+1
print(m*n)

##Fourth Program

Que="A1:A1"
p=Que.split(":")

a=p[0][0]
b=p[1][0]

c=p[0][1:]
d=p[1][1:]

if (a == b and c == d):
    print("Invalid")
else:
    m = abs(int(c)-int(d))+1
    n = abs(ord(a)-ord(b))+1
print(m*n)
## Vaccination Drive List Preparator

def fun(a, d, c):
    la = len(a)
    ld = len(d)
    if not(la==14 or ld==10 or c=="no" or c=="yes"):
        print("Invalid Input")
    else:
        s = d.split('/')
        age = 2021-int(s[-1])
        if age>60 or c=="yes":
            print(1)
        elif age>45:
            print(2)
        elif age>30:
            print(3)



fun("6785 3456 1237","03/12/192","no")



#Magic Numbers[The aim is to find the magic numbers.]
def MagicNumber(u,o):
    ans = []
    for i in a:
        if len(str(i))==3:
            ans.append(i)
    print(ans)
    ans.sort()
    print(ans[o-1])
    pass











u = int(input())
a = [0]*u
for i in range(u):
    a[i]=int(input())
o = int(input())
MagicNumber(u,o)

#Reverse the word in a given sentence
def findthereverseword(a):
    print(a)







y = input()
findthereverseword(a)
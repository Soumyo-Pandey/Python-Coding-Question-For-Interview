#data to a new Server(wipro)
n = int(input())
a = list(map(int,input().split()))
for a in a:
    b = bin(a)[2:]
    ans=""
    for i in b:
        if (i=='1'):
             ans=ans+'0'
        else:
            ans=ans+'1'

    python = int(ans,2)
    print(python, end = " ")
print('\n')



#house construction
def costOfGarden(side, length, breadth, cost):
    ans = 0
    if (side<=0 or length<=0 or breadth<=0 or cost<=0 or side<length or side<breadth):
         print("Invalid Input")
    else:
          ss = side*side
          areah = length*breadth
          t = ss-areah
          ans = (t*cost)//100
          print(ans)
          print('\n')

costOfGarden(50,40,35,65);


#Trailing Zeros
n=100
ans=0
while(n!=0):
    n=n//5
    ans+=n
print(ans)


#Find Third last consonant

a=input()
c=0
ans=''
for i in range(len(a)-1,-1,-1):
    if (c<3 and (not a[i]=='a') and (not a[i]=='e') and (not a[i]=='i') and (not a[i]=='o') and (not a[i]=='u')):
        ans=a[i]
        c+=1
        
print(ans)
print('\n')

#Dice Problem(6th may 2021)

t=int(input())
count = 0
if t>=0 and t<=12:
    for i in range(1, 7):
        for j in range(1, 7):
             if i+j==t:
                 count+=1
    print(count)
else:
     print(0)

print('\n')

#Numbering of house is done by Municipal Of India[TCS Coding]
z = int(input())
odd = []
even = []
for i in range(z):
    k = int(input())
    if k%2 == 0:
        even.append(k)
    else:
        odd.append(k)
even.sort()
odd.sort()
print(odd,even)


#IBM Coding Question[Number of words written on given line of a page]
def this_find_answer(firstpage,secondpage,finalcountofpage):
    a=firstpage 
    b=secondpage
    c=finalcountofpage
    if(a>b) or (a<=0) or (b<=0):
       print("Invalid input")
    else:
        arr=[0]*c #int arr[c]
        arr[0]=a
        arr[1]=b
        for i in range(2,c):
            arr[i] = arr[i-1]+arr[i-2]
        print(arr[c-1])

this_find_answer(1,2,5)
this_find_answer(1,10,3)

#Wipro Coding Array
a,b = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(arr[-b])
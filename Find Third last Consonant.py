a = input()
c=0
ans=''
for i in range(len(a)-1,-1,-1):
  if(c<3 and (not a[i]=='a') and (not a[i]=='e') and (not a[i]=='i') and (not a[i]=='o') and (not a[i]=='u')):
    ans = a[i]
    c+=1
print(ans)

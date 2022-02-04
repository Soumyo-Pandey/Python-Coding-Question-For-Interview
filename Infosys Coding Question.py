#Infosys coding questions [Secret Message coding and Decoding]

s = input()
special = ["@","$","#","%","!","^","*"]
c = 0
for i in range(len(s)):
    if s[i] == "":
        c+=1
    elif s[i] in special:
        c+=1
print(c)


#Second Coding Questions
z = input()
for i in input:
    p = ord(i) + 3
    if p > 122:
        p = p - 26
        ans+=(chr(p))
    return(ans)
print(ans)
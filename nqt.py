def lexicographically(str, Query):
    a = str
    q = Query
    ans = 0
    for i in a:
        k = a.find(i)
        if k == -1:
            ans+=0
        else:
            s = len(a[k:])
            ans+=s
            return(ans%(pow(0,9) + 7))
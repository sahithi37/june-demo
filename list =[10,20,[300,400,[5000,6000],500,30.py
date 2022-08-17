list =[[10],[20],[300,400,[5000,6000],500,30,40]]
s=[]
c=0
for i in list:
    c+=1
    if len(i)==1:
        s.append(i)
    else:
        
        p=0
        for j in i:
            p+=1
            s.append(j)
            if j == 6000:
                s[c][p].insert(p+1,7000)
print(s)
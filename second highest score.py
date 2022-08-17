n = int(input())
l = []
for i in range(n):
    name = input()
    score = float(input())
    l.append([name,score])

for i in range(n):
    for j in range(i+1,n):
        if l[i][1]>l[j][1]:
            temp = l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
m=[]
for i in range(n):
        m.append(l[i][1])
print(m)
s=[]
s.append(m[0])
for i in m:
    if i in s:
        pass
    else:
        s.append(i)
print(s)

k=[]
for i in range(n):
    if s[1] == l[i][1]:
        k.append(l[i])
k.sort()
    
print(k)
for i in k:
    print(i[0])




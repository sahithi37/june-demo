
def matrix(a,p,q):
    for i in range(p):
        print(a[i])
    







n=int(input())
m=int(input())
K=[]
for i in range(n):
    P=map(int,input().split()[:m])
    K.append(list(P))
    print()
matrix(K,n,m)
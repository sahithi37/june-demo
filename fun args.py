def avg(*a):
    k=0
    m=0
    for i in a:
        k+=1
        m+=i
        val = m/k
    return val




print(avg(1,2,3,4))
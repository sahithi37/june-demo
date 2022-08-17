class Stats():
    def __init__(self,a):
        self.items=a
    def mean(self):
        s=0
        m=0
        for i in self.items:
            s+=1
            m+=i
        k = m/s
        print("mean:",k)
    def median(self):
        for i in range(len(self.items)):
            for j in range(i+1,len(self.items)):
                if(self.items[i]>self.items[j]):
                    temp = self.items[i]
                    self.items[i] = self.items[j]
                    self.items[j] = temp
        if len(self.items)%2==0:
            p = len(self.items)//2
            q=self.items[p-1]
            r=self.items[p]
            print("median:",(q+r)/2)
        else:
            print("median:",self.items[(len(self.items)//2)+1])
    def mode(self):
        t=[]
        q=0
        t.append(self.items[0])
        for j in self.items:
            if j in t:
                pass
            else:
                t.append(j)
        print(t)
        h=[]
        w=[]
        for i in range(len(t)):
            u = 0
    
            for j in range(len(self.items)):
                if t[i]==self.items[j]:
                    u+=1
            w.append(u)
        e=[]
        e.append(w[0])
        for i in range(len(e)):
            for j in range(len(w)):
                if e[i]==w[j]:
                    pass
                else:
                    e.append(w[j])
        v=0
        for i in range(len(e)):
            if(e[i]>v):
                v=e[i]
        for j in range(len(w)):
            if v==w[j]:
                print(t[j])
            
stat = Stats([10,30,20,20,40,50,10,20])
stat.mean()
stat.median()
stat.mode()
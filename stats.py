class Stats():
    def __init__(self,a):
        self.items=a
    def mode(self):
        t=[]
        q=0
        t.append(self.items[0])
        for i in range(len(self.items)):
            for j in range(len(t)):
                if self.items[i]==t[j]:
                    q+=1
            if q==0:
                t.append(self.items[i])
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
stat.mode()
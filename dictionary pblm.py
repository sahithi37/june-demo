n = int(input())
student_marks = {}
for i in range(n):
    name= input()
    scores = list(map(float, input().split()))
    student_marks[name] = scores
name_1 = input()
avg = 0
for j in student_marks.items():
       if name_1 == j[0]:
            for k in j[1]:
                avg+= k
            m=avg/n

print(round(m,2))

        

        






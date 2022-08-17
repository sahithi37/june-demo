def sports():
    return 200

score=sports()

with open("file.txt") as f:
    line = f.readlines()
    print(line)
    k=-1
    for i in line:
        k+=1
        value = int(i)
        if value < score or value == " ":
            line[k] = (str(score))
            with open("file.txt","w") as f:
                f.writelines(line)
        
        else:
            with open("file.txt","w") as f:
                line[k]=str(value)
                f.writelines(line)
    

path = input("Input file path/filename: ")

f = open(path, mode='r')

content = f.read()

f.close()

pos1 = 0
pos2 = 0
i = 0
isCompleted = False
found = False
tempcontent1 = ""
tempcontent2 = ""

while True:
    if i >= len(content)-1:
        break
    
    print(i)

    if content[i:i+7] == "<anime>":
        pos1 = i
        
        y = i
        while True:
            if content[y:y+9] == "Completed":
                isCompleted = True
            
            if content[y:y+8] == "</anime>":
                pos2 = y+8
                found = True
                break
            
            y+=1
        
    if found:
        found = False
        
        if not isCompleted:
            tempcontent1 = content[:pos1]
            tempcontent2 = content[pos2:]
            content = tempcontent1 + tempcontent2
    
    isCompleted = False
    
    i+=1
    
o = open("output.xml", mode='w')

o.write(content)

o.close()

exit()
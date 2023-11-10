#!/usr/bin/python3

f = open("movies_exp.txt", "rt")
t = open("movie.dat", "wt")
q = open("movieoutput.txt", "wt")
wordcount = {}

while True:
    line = f.readline()
    if line == '' :
        break
    print(line, end='')
    seperate = line.split("::")
    i = 0
    for s in seperate:
        if(i == 0):
            lines = ("ID : ", s)
            t.writelines(lines)
        elif(i == 1):
            lines = (", Title(year) : ", s)
            t.writelines(lines)
        else:
            lines = (", Genre : ", s)
            t.writelines(lines)
                        
        i += 1

t.close()
t = open("movie.dat", "rt")

while True:
    line2 = t.readline()
    if line2 == '' :
        break
    print(line2, end='')
    seperate2 = line2.split(", Genre : ")
    z = 0
    for s1 in seperate2:
        if(z == 1):
            words = s1.split("|")
            for word in words:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
                        
        z += 1

for key, value in wordcount.items():
    k = (str)(key)
    v = (str)(value)
    item2 = (k, " ", v, "\n")
    q.writelines(item2)
    
t.close()
f.close()
q.close

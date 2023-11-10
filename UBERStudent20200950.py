#!/usr/bin/python3

f = open("uber_exp.txt", "rt")
t = open("uber.txt", "wt")
q = open("uberoutput.txt", "wt")
wordcount = {}

while True:
    line = f.readline()
    if line == '' :
        break
    print(line, end='')
    seperate = line.split(",")
    i = 0
    for s in seperate:
        if(i == 0):
            lines = ("Base number : ", s)
            t.writelines(lines)
        elif(i == 1):
            lines = (", Date : ", s)
            t.writelines(lines)
        elif(i == 2):
            lines = (", active vehicles : ", s)
            t.writelines(lines)
        else:
            lines = (", trips : ", s)
            t.writelines(lines)
                        
        i += 1
    
t.close()
f.close()
q.close
import os

def kortejkataloga(filename):
    lst1 = []
    lst2 = []
    for i in os.listdir(filename):
        if (os.path.isfile(filename + '/' + i) == True):
            lst1.append(i)
        else:
            lst2.append(i)
    return (lst1, lst2)
    
print(kortejkataloga('/home/stud/PythonProjects/lab3_files'))

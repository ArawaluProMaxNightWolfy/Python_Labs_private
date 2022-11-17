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
    




def oof(file, n=4):
    if (kortejkataloga(file)[0] != []):
        for i in kortejkataloga(file)[0]:
            print(' '*n + i)
    if (kortejkataloga(file)[1] != []):
        for i in kortejkataloga(file)[1]:
            print(' '*n + i)
            oof(file +'/'+ i, n + 4)
oof('/home/stud/PythonProjects/lab3_files')
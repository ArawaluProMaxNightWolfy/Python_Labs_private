from pathlib import Path

def kortejkataloga(filename):
    lst1 = []
    lst2 = []
    for i in Path(filename).iterdir():
        if (Path(i).is_file() == True):
            lst1.append(i)
        else:
            lst2.append(i)
    return (lst1, lst2)
    




def oof(file, file_tag='*.py', n=4):
    if (kortejkataloga(file)[0] != []):
        for i in Path(file).glob(file_tag):
            print(' '*n + str(i))
    if (kortejkataloga(file)[1] != []):
        for i in kortejkataloga(file)[1]:
            oof(file = file +'/'+ str(i).split('/')[-1], file_tag='*.py', n = n + 4)
oof('/home/stud/PythonProjects/Raspakovka')
import shutil
import os

#shutil.make_archive('cool_archive', 'bztar')
def raspakovka(filename, extract_dir=os.getcwd()+'/Raspakovka', copy_dir=os.getcwd(), mask='*.py'):

    shutil.unpack_archive(filename, extract_dir)
    shutil.copytree(extract_dir, os.getcwd()+'/Sortirovka', ignore=shutil.ignore_patterns(mask))
    #shutil.make_archive(filename.split('.')[0] +'(1)'+ filename.split('.')[1], 'bztar', copy_dir, os.getcwd()+'/Sortirovka')








a = str(input('filename: '))
#b = str(input('extract_dir: '))
#c = str(input('copy_dir: '))
#d = str(input('mask: '))
raspakovka(a)
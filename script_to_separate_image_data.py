import os, shutil

f1 = '29.3.22/JPG/'  #input directory or Path
d1 = os.listdir(f1)   
f2 = '29.3.22/PNG/'  #input directory or Path 
d2 = os.listdir(f2)
f1new = '29.3.22/orig/'  #output path or directory
f2new = '29.3.22/tr' #output path or directory 

def comparecopy():
    files = list(set(d1) & set(d2))    # compare statement
    #print(files)
    for f in files:
        shutil.copy(os.path.join(f1, f), f1new)    # copy - copies file
        shutil.copy(os.path.join(f2, f), f2new)   # move - to move file
    print('Compare & copy successful')

if __name__ == '__main__':
    comparecopy()
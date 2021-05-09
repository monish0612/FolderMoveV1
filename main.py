import shutil
import os

def foldermove(oldpath,newpath):
    oldpathexists=os.path.isdir(oldpath)
    if oldpathexists:
        newpath = newpath+f"\\{os.path.basename(oldpath)}"
        newpathexists = os.path.isdir(newpath)
        if newpathexists==False:
            shutil.copytree(oldpath,newpath)

        else:
            print('Destination directory already exists')
            return 'Destination directory already exists'


    else:
        print('Source directory does not exists')
        return 'Source directory does not exists'



foldermove("C:\\Users\\monis\\Downloads\\SourceFolder","D:\\Programs")

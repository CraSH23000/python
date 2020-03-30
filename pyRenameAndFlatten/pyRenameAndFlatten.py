import os, shutil
from pathlib import Path
#C:\\tmp3\\
#C:\\tmp4\\
source = "C:\\tmp3\\"
moveto = "C:\\tmp4\\"
fileExtension = '.txt'

# create directory
if not os.path.exists(moveto):
    os.makedirs(moveto)

files = os.listdir(source)
files.sort()

filename = 'indexFile.txt'
if os.path.exists(moveto+filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

indexFile = open(moveto+filename,append_write)
pathlist = Path(source).glob('**/*.*')

for i, path in enumerate(pathlist):
    # because path is object not string
    spath = str(path)
    start = spath.find(source) + len(source)

    if spath.rfind('\\', start) == -1:
        # no folder to append to file name
        f2 = str(i)+fileExtension
    else:
        end = spath.rfind('\\', start)
        folder = spath[start:end]
        f2 = str(i)+'_'+folder+fileExtension # use folder

    msg = f2+' was '+spath[start:len(spath)]
    indexFile.write(msg+'\n')
    print(msg)
    dst = moveto+f2
    shutil.move(spath,dst)
indexFile.close()

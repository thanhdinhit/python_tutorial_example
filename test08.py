import os
ROOT_DIR = os.path.abspath(os.curdir)
print (ROOT_DIR)
arr = os.listdir()
print (arr)
files_path = [os.path.abspath(x) for x in os.listdir()]
print(files_path)

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
arr01 = []
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".py"):
            arr01.append((os.path.join(r, file)))
            print(os.path.join(r, file))
print(arr01)
print(arr01[2].replace('\\', '/'))




# import shutil
# shutil.copy('/Test01/readme.txt', '/Test02')
# shutil.copyfile('/Test01/readme.txt', '\Test02')
# copy and create folder
# shutil.copytree(r'C:\Users\dinhnt15\Desktop\DinhNt15\Python\Test01', r'C:\Users\dinhnt15\Desktop\DinhNt15\Python\Test03')

import shutil
import os
 
# path to source directory
src_dir = 'Test01'
 
# path to destination directory
dest_dir = 'Test04'
 
# getting all the files in the source directory
files = os.listdir(src_dir)
 
shutil.copytree(src_dir, dest_dir)
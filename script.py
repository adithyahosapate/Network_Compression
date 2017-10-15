import os
import shutil
Main_file_list=[]
for dirName, subdirList, fileList in os.walk("../Network_Compression"):
	for fname in fileList:
		Main_file_list.append(dirName+"/"+fname)
	#print(len(list(A)))
dstroot = 'new_folder/'


# assert not os.path.isabs(srcfile)
# dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))

# os.makedirs(dstdir) # create all directories, raise an error if it already exists
# shutil.copy(srcfile, dstdir)

for path in Main_file_list:

	shutil.copy(path,dstroot)	
'''
date:		06/12/2019
author:		Stacy Bridges
info:		this script gets metadata for files in
			a directory tree:
            - filename

st_mode
File mode: file type and file mode bits (permissions).

st_ino
Platform dependent, but if non-zero, uniquely identifies the file for a
 given value of st_dev. Typically:
	the inode number on Unix,
	the file index on Windows

st_dev
Identifier of the device on which this file resides.

st_nlink
Number of hard links.

st_uid
User identifier of the file owner.

st_gid
Group identifier of the file owner.

st_size
Size of the file in bytes, if it is a regular file or a symbolic link.
The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
Timestamps:
	st_atime
Time of most recent access expressed in seconds.
	st_mtime
Time of most recent content modification expressed in seconds.
	st_ctime
Platform dependent:
the time of creation on Windows, expressed in seconds.
	st_atime_ns
Time of most recent access expressed in nanoseconds as an integer.
	st_mtime_ns
Time of most recent content modification expressed in nanoseconds as an integer.
	st_ctime_ns
Platform dependent:
the time of creation on Windows, expressed in nanoseconds as an integer.
'''
# IMPORTS  =======================================
import os
import os.path
from pathlib import Path
import math
from datetime import datetime

# GLOBALS  =======================================

# FUNCTIONS  =====================================

# MAIN  ==========================================
def main():
	f_names_l = []  # file names
	f_size_l = []  # file size in kb
	f_access_l = []  # last time accessed
	f_modify_l = []  # last time modified

	fnames = os.listdir()
	for f in fnames:
		f_names_l.append(f)
		#print('File name: ', f)

	with os.scandir() as dir_entries:
		for entry in dir_entries:
			info = entry.stat()
			f_size_l.append(info.st_mtime)  # file size in kb
			f_access_l.append(info.st_atime)
			f_modify_l.append(info.st_mtime)


	print('------------------------')
	i = 0
	for n in f_names_l:
		print('File name:\t', f_names_l[i])
		print('File size:\t', math.trunc(f_size_l[i]/1000000), 'KB')
		print('Last accessed:\t', f_access_l[i])
		print('Last modified:\t', f_modify_l[i])
		print('\n')
		i += 1

	# print(Path(r"NA1600149.Ormat.Forge21-31_w_reamer.Churchill.NV.HD.Rev-8.xlsx").stat())


if __name__ == '__main__': main()

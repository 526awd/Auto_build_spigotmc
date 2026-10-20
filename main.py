import os
import sys

filever=sys.argv[1:][0]
ver_list_file=open(filever)
ver_list=ver_list_file.readlines()
ver_list_file.close()
for i in ver_list:
    i=i.rstrip('\n')
print(ver_list)
os.system
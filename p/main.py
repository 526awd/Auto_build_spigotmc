import os
import sys

filever=sys.argv[1:][0]
ver_list_file=open(filever)
ver_list=ver_list_file.readlines()
ver_list_file.close()

print(ver_list)
for i in ver_list:
    os.system("java -jar BuildTools.jar --rev "+i.rstrip('\n')+" --output-dir ../out/")
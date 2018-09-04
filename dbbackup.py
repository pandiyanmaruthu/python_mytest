import os
file="dbfile"
if (os.path.exists(file)):
    file1=open(file)
    print ("db found")
else:
    print("db not found")
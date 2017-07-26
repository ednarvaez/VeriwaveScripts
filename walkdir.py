import os

# os.path.join (path, file)



path = "/tmp/python"

# List everything

print (os.listdir(path))

# Walk directories.

for dirpath, dirname, filename in os.walk(path):
    print ('Current Path:', dirpath)
    print ('Directories:', dirname)
    print ('Files', filename)

    print ('Complete Pathname: ', os.path.join (dirpath, path))

    print ()




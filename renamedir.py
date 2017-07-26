import os
os.chdir('/Users/enarvaez/Downloads/02.00.01.38/5G/LAN')

dut = raw_input('DUT (Ex. BHR4): ')
version = raw_input('Firmware Version (01.04.00.863): ' )
port = raw_input('LAN or WAN: ')

print dut, version, port

print (os.getcwd())

for f_orig in os.listdir(os.getcwd()):
    #print f_orig
    f_new = f_orig[16:]
    #print f_orig, f_new
    #os.renames (f_orig, f_new)
    print f_orig, f_new


ok = raw_input("Be careful.   OK to continue (yes/no)?  ")
if ok == 'yes':
    print ("Renaming folders")
    for f_orig in (os.listdir(os.getcwd())):
        # print f_orig
        # strip first 15 characters - timestamp
        f_new = f_orig[16:]
        #os.renames (f_orig, f_new)
        print f_orig, " is renamed to ", f_new

if ok == 'no':
    exit()




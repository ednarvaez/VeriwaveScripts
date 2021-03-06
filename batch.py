import os, time, random
#os.chdir('/Users/enarvaez/Downloads/02.00.01.38/5G/LAN')

##########  Get User Input

directory = raw_input ('Script Directory: ')
dut = raw_input('DUT (Ex. BHR4): ')
version = raw_input('Firmware Version (Ex. 01.04.00.863): ' )
port = raw_input('Direction (Ex LAN): ')

os.chdir(directory)

#print dut + '-' + version + '-' + port + '-'
#print ('Current Direcotry is: ', os.getcwd())

def findnewestdir ():
    ######## find newest directory
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    return (latest_subdir)

######## run tests

alltests = [
    '5g-udp-dn-1c.wml',
    '5g-udp-dn-25c.wml',
    '5g-udp-up-1c.wml',
    '5g-udp-up-25c.wml',
    '5g-udp-bidir-1c.wml',
    '5g-udp-bidir-25c.wml' ]


for test in alltests:
    # os.system('./test.sh')
    os.system('mkdir ' + (str(random.randint(0,9))))
    time.sleep(65)
    print('Newest Directory: ', findnewestdir())
    dutdetails = (dut + '-' + version + '-' + port)
    os.renames (findnewestdir(), findnewestdir() + '-' + dutdetails + '-' + test[:-5])
    #print (dutdetails)
    print ('Directory just created: ', findnewestdir() + '-' + dutdetails + test[:-5])
    #print (dut + '-' + version + '-' + port + '-' + test[:-3])



# os.system('"C:\Program Files (x86)\VeriWave\waveapps_cl.exe"')
# subprocess.call(['C:\Program Files (x86)\VeriWave\waveapps_cl.exe', '-s', '5g-tcp-bidir-1c-1s.wml']) 



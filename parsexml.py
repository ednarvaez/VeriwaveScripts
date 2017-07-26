'''
Walk resuts directory, parse each csv, populate another spreadsheet with results
'''

import os, csv


#directory = raw_input ('Results Directory: ')

directory = '/tmp/python'
os.chdir(directory)
print os.getcwd()
print os.listdir(directory)


# Ask for name of sumamary spreadsheet

print ()
summaryresults = raw_input ('Provide of Summary Results .csv File: ')
csvFile = open(summaryresults, 'w')
csvWriter = csv.writer(csvFile)


#####   Walk directories, Load TCP/UDP Results .csv file and write to draft export


for root,dirs,files in os.walk(directory):
    #print ('Folder: ', root)
    for file in files:
        #   GET TCP DATA
        if file.startswith("Results_tcp_goodput.csv"):
            print ('AbsPath: ', os.path.join(root, file))
            print ('Subfolder: ', root)
            data = open (os.path.join(root, file))
            dataread = csv.reader(data)
            datalist = list(dataread)
            #result536 = ((datalist[12][1]), (datalist[12][2]))
            #result1460 = ((datalist[13][1]), (datalist[13][2]))
            #print result536
            #print result1460
            csvWriter.writerow ([root, datalist[12][1], datalist[12][2]])
            csvWriter.writerow ([root, datalist[13][1], datalist[13][2]])


        #  GET UDP DATA
        if file.startswith("Results_unicast_through1put.csv"):
            print ('AbsPath: ', os.path.join(root, file))
            print ('Subfolder: ', root)
            udpdata = open (os.path.join(root, file))
            udpdataread = csv.reader(udpdata)
            udpdatalist = list(udpdataread)
            # retrieve UDP Throughput per Frame Size
            for i in range (14, 22):
                #print ((udpdatalist[i][0]), udpdatalist[i][7])
                udpresult = ((udpdatalist[i][0]), udpdatalist[i][7])
                csvWriter.writerow([root, udpdatalist[i][0], udpdatalist[i][7]])



csvFile.close()

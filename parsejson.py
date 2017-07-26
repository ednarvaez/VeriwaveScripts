import json
import os
# from pprint import pprint

# os.chdir('/Users/enarvaez/Downloads/02.00.01.38/5G/LAN')

#print (os.getcwd())
#file = (os.getcwd(),"/Results_tcp_goodput.json"

with open('/Users/enarvaez/Downloads/02.00.01.38/5G/LAN/BHR4-5G-2.0.1.38-LAN-TCPBIDIR-1c-1s/Results_tcp_goodput.json') as data_file:
    data = json.load(data_file)

#with open('strings.json') as json_data
#    d = json.load(json_data)


# pprint (data)

data["Status"]

# print (data["Config"]["Test"])
print ()
print ("Test:       " + data["Config"]["Test"]["Name"])
#print ("Mapping:    " + data["Config"]["Test"]["TrafficDir"])
print ("Mapping:    " + data["Config"]["Mapping"]["Map"])
print ("Direction:  " + data["Config"]["Mapping"]["Direction"])
print ("# Clients:  " + data["Config"]["Test"]["NumOfSessionPerClient"])
print ("# Sessions: " + data["Config"]["Test"]["NumOfSessionPerClient"])
print ("LAN/WAN:    " + data["Config"]["ClientGroups"]["RF"]["PortName"])



#if data["Config"]["Test"]["TrafficDir"]) eq "Ethernet To Wireless":


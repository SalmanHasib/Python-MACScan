#!/usr/bin/python

import os
import nmap
from nmap import PortScanner as pscan
import pprint

pp = pprint.PrettyPrinter(indent=4)
whitelist = []
unknown = []
whitepath = os.environ["HOME"] + "/path/to/some/directory/"
with open(whitepath) as fw:
    for line in fw:
        whitelist.append(line.strip().upper())
fw.closed

unknownpath = os.environ["HOME"] + "/path/to/same/whitelist/directory/"
with open(unknownpath) as fu:
    for line in fu:
        if line.strip() not in whitelist:
            unknown.append(line.strip().upper())
fu.closed

result = pscan().scan('192.168.1.*').get('scan')
for ipaddr, value in result.iteritems():
    if(value.get('addresses').get('ipv4') != "192.168.1.208"):
        mac = value.get('addresses').get('mac')
        if(mac == None or type(mac) == 'Nonetype'):
            print "No MAC address:\n"
            print pp.pprint(value)
        else:
            if mac not in whitelist:
                if mac not in unknown:
                    unknown.append(mac.upper())

unknownfile = open('unknowns.txt','w+')
for mac in unknown:
    unknownfile.write("%s\n" % mac)
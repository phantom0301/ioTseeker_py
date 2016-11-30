#! /usr/bin/env python
# -*- coding:utf-8  -*-

import requests
import base64
import json
import re
import sys

devs = {}
headers = {}
devType = ""
ipList = []
ptr = -1
httpPort = 80
debug = 0
ip = sys.argv[1]

def readDevices():
    if devCfgUrl == "":
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(devCfgUrl, verify=False, headers=headers)
        buff = req.content
    else:
        with open('devices.cfg') as f:
            buff = f.read()
        f.close()
    devs = json.loads(buff)
    return devs

def ip2num(ip):
    a = re.split('\.', ip)
    return (a[0]<<24) + (a[1]<<16) + (a[2]<<8) +a[3]

def num2ip(n):
    return str((n >> 24))+'.'+str((n >> 16)&0xff)+'.'+str((n >> 8)&0xff)+'.'+str(n&0xff)


if re.match("^\-?h", sys.argv[1]):
    print "python iotScanner.py <ipRanges> [devCfgUrl=<devCfgUrl>]\n"

devCfgUrl = ""
for i in range(len(sys.argv)):
    if re.match("devCfgUrl=", sys.argv[i]):
        devCfgUrl = sys.argv[i][10:]
    elif re.match("^debug", sys.argv[i]):
        debug = sys.argv[i][5:]
    else:
        debug = 1

devs = readDevices()

for e in re.split('\,', sys.argv[1]):
    if re.findall('\-', e):
        start = "before re"
        end = "after re"
        print start+'|'+end+'|'+'\n'
        for i in range(ip2num(start), ip2num(end)):
            ipList.append(num2ip(i))
    else:
        ipList.append(e)




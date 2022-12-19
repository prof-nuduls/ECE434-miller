#!/usr/bin/env python3
import time

eQEP = '2'
COUNTERPATH = '/dev/bone/counter/'+eQEP+'/count0'

ms = 100
maxCount = '1000000'

f = open(COUNTERPATH+'/ceiling','w')
f.write(maxCount)
f.close()

f = open(COUNTERPATH+'/enable','w')
f.write('1')
f.close()
f = open(COUNTERPATH+'/count','r')

olddata = -1
while True:
    f.seek(0)
    data = f.read()[:-1]
    if data != olddata:
        print("data = " +data)
    time.sleep(ms/1000)


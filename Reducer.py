#!/usr/bin/python
import sys

current=None
count=0

for line in sys.stdin:

    key,val=line.strip().split("\t")
    val=int(val)

    if current==key:
        count+=val
    else:
        if current:
            print(current+"\t"+str(count))

        current=key
        count=val

if current:
    print(current+"\t"+str(count))

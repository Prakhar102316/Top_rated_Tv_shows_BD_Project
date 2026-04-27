#!/usr/bin/python
import sys

next(sys.stdin)

for line in sys.stdin:

    fields=line.strip().split(",")

    if len(fields)<5:
        continue

    try:
        rating=float(fields[4])

        if rating >= 8.5:
            print("HighRated\t1")
        else:
            print("MediumRated\t1")

    except:
        continue

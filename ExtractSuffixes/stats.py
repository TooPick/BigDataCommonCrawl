#!/usr/bin/env python

import sys
import numbers

total = 0
lines = sys.stdin.readlines()
for line in lines:
    	line = line.strip()
    	keys = line.split()
	if len(keys) > 1:
		total += float(keys[1])

print "Total TLD : {0}".format(total)

for line in lines:
	line = line.strip()
	keys = line.split()
	if len(keys) > 1:
		percent = "%.6f" % ((float(keys[1]) * 100) / total)
		print("{0}\t{1}\t{2}%".format(keys[0],keys[1],percent))

#!/usr/bin/env python

import sys
import numbers

for line in sys.stdin:
    line = line.strip()
    keys = line.split(')')
    names = keys[0].split(',')

    if len(names) > 1 and not names[0].isdigit():
	if(names[0] == "fr"):
    		print('{0}\t{1}'.format(names[1]+"."+names[0], 1))

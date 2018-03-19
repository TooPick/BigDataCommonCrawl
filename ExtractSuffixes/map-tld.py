#!/usr/bin/env python

import sys
import numbers

for line in sys.stdin:
    line = line.strip()
    keys = line.split(',')

    if len(keys) > 1:
    	print('{0}\t{1}'.format(keys[0], 1))

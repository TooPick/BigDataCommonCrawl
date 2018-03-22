#!/usr/bin/env python

import sys

last_key      = None              
running_total = 0

for input_line in sys.stdin:
    input_line = input_line.strip()

    this_key, value = input_line.split("\t", 1)  
                          
    value = int(value)           

    if last_key == this_key:    
        running_total += value   

    else:
        if last_key:  
		domain = last_key.split(',')           
            	print( "{0}.{1}".format(domain[1], domain[0]) )
                                
        running_total = value    
        last_key = this_key

if last_key == this_key:
	domain = last_key.split(',')
    	print( "{0}.{1}".format(domain[1], domain[0])) 
	


#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys, os, random


def main():
    # look at sys module
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    
    # look at os module
    osModules = (
         os.name,
         os.getenv('PATH'),
         os.getcwd(),
         os.urandom(12),
         os.urandom(12).hex()
    )
    for i in osModules:
        print(i, end = '\n\n')
        
    # look at random module

if __name__ == '__main__': main()

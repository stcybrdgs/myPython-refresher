#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys, os, random, datetime


def main():
    # look at sys module
    print('SYS Module: ============================')
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v), '\n')
    
    # look at os module
    print('OS Module: ============================')
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
    print('Random Module: ============================')
    randomModules = (
        random.randint(1, 1000),
        't'
    )
    for i in randomModules:
        print(i, end = '\n\n')
        
    myList = list(range(25))
    random.shuffle(myList)
    print(myList)
    
    # look at datetime module
    print('\nDatetime Module: ============================')
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    
if __name__ == '__main__': main()

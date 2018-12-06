#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test simplest multiprocessing functionality.

Usage:
./multiprocessing_simpleargs.py
python multiprocessing_simpleargs.py

Input Variables:
		None.

Reference: 
https://pymotw.com/2/multiprocessing/basics.html 

Created on 2016 Sep 8 by Edwin Campos
Last modification on 2018 Dec 6 by Edwin Campos
@author: ecampos.phd@gmail.com
To access this Docstring in the Python console, type 'ComputeFcstSkillWxAgg.__doc__'
"""

# Dependencies
import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

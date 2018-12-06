#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test multiprocessing functionality.

Usage:
./multiprocessing_exitcode.py
python multiprocessing_exitcode.py

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
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        print 'Starting process for', f.func_name
        j = multiprocessing.Process(target=f, name=f.func_name)
        jobs.append(j)
        j.start()
        
    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print '%s.exitcode = %s' % (j.name, j.exitcode)

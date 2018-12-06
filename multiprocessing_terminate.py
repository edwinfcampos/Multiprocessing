#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test how to terminate multiprocessing.

Usage:
./multiprocessing_terminate.py
python multiprocessing_terminate.py

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
import time

def slow_worker():
    print 'Starting worker'
    time.sleep(0.1)
    print 'Finished worker'

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive()
    
    p.start()
    print 'DURING:', p, p.is_alive()
    
    p.terminate()
    print 'TERMINATED:', p, p.is_alive()

    p.join()
    print 'JOINED:', p, p.is_alive()

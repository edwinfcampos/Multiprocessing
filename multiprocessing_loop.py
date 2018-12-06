#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test multiprocessing functionality within a loop.

Usage:
./multiprocessing_loop.py
python multiprocessing_loop.py

Input Variables:
		None.

Reference: 
https://docs.python.org/2/library/multiprocessing.html 

Created on 2016 Sep 9 by Edwin Campos
Last modification on 2018 Dec 6 by Edwin Campos
@author: ecampos.phd@gmail.com
To access this Docstring in the Python console, type 'ComputeFcstSkillWxAgg.__doc__'
"""

# Dependencies
import datetime
startTime = datetime.datetime.now()
import multiprocessing
import pandas as pd
import time

# Constants
HOW_MANY_SITES = 5
METHOD = 0  # A value of zero is recommended   

def workerTask(num):
    """thread worker function"""
    df = pd.DataFrame({'a':range(3), 'b':range(3)})    
    print 'Worker:', num
    time.sleep(20)  # Wait 20 seconds
    return df

if __name__ == '__main__':
    fullDataFrame = pd.DataFrame()  # Define empty Pandas dataframe     
    pool = multiprocessing.Pool(processes=HOW_MANY_SITES)   # Start all worker processes
    if METHOD == 0:   # Multiple/parallel processing
    	resultsList = []   # Initializing as an empty list
    	for i in range(HOW_MANY_SITES):
            poolResults = pool.apply_async(workerTask, (i,))
	    resultsList.append(poolResults) 
    	for result in resultsList:
    	#for result in poolResults.get():
	    #indxDataFrame = result.get()
	    fullDataFrame = fullDataFrame.append(result.get())
    elif METHOD == 1:  # Not really using multiple/parallel processing !
	for i in range(HOW_MANY_SITES):
             poolResults = pool.apply_async(workerTask, (i,))
             fullDataFrame = fullDataFrame.append(poolResults.get())
    else:   # Single processing, in series
	for i in range(HOW_MANY_SITES):
	     indxDataFrame = workerTask(i)
	     fullDataFrame = fullDataFrame.append(indxDataFrame)

    print 'len(fullDataFrame) = %s' % len(fullDataFrame)
    print fullDataFrame
    endTime = datetime.datetime.now()
    print 'With METHOD = %s, this code ran in %s seconds.' % ( METHOD, str((endTime - startTime).seconds) )
    #print 'This code ran in ' + str( (endTime - startTime).seconds/60.0 ) + ' minutes.'

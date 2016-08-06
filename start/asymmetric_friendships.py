# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:21:53 2016

@author: xingdu
"""


import MapReduce
import sys

"""
Social Network dataset with friends counting in the Simple Python MapReduce Framework
Test Input: friends.json
Test Output: friend_count.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person A
    # value: just a single count indicating record[1] is a friend with 'key'
    name = record[0]
    friend=record[1]
    mr.emit_intermediate(tuple(sorted((name,friend))),1)

def reducer(key,list_of_values):
        total=0
        for v in list_of_values:
                total +=v
        if total==1:
                mr.emit(key)
                mr.emit(key[::-1])

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
                                      
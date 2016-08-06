# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:10:59 2016

@author: xingdu
"""

import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
        key=record[1]
        mr.emit_intermediate(key,record)

def reducer(key,list_of_values):
        for v1 in list_of_values:
                for v2 in list_of_values:
                        if v1[0]>v2[0]:
                                res=v1+v2
                                mr.emit(res)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
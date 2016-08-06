# -*- coding: utf-8 -*-
"""
Created on Mon May 16 02:04:08 2016

@author: xingdu
"""
#use Python3

def get_fibonacci_last_digit(n):
    # write your code here
    if (n<=1):
        return n;
    else:
        fibs=[0,1]
        for i in range(2,n+1):
                fibs.append((fibs[-1]%10)+(fibs[-2]%10))
                fibs=fibs[1:]
        return fibs[1]%10

n = int(input())
print(get_fibonacci_last_digit(n))

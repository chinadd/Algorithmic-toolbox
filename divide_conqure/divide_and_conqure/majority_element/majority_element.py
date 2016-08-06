# Uses python3

import sys
"""
from collections import Counter
def most_common(lst):
    dict={}
    for i in range(len(a)):
        if a[i] not in dict.keys():
           dict[a[i]]=1
        elif a[i] in dict.keys():
           dict[a[i]]+=1
    
    return max(dict, key=dict.get)

def get_majority_element(a, left, right):
    c = Counter(a)
    value, count = c.most_common()[0]
    if left == right:
        return -1
    elif left + 1 == right:
        return a[left]
    #write your code here   
    else:
        if a.count(most_common(a)) > round(len(a)/2):
        #if count > round(len(a)/2):
            return 1
        
    return -1
"""
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_m = get_majority_element(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element(a, (left + right - 1)//2 + 1, right)
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

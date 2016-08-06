# Uses python3
import sys

def binary_search(a, x):
    return bin_search(a,x,0,len(a)-1)

def bin_search(a,x,start,end):
    left, right = start, end
    mid=int((left+right)/2)
    #print(mid)
    if right<left:
        return -1

    if a[mid]==x:
        return mid
    elif a[mid]<x:
        return bin_search(a,x,mid+1,right)
    else:
        return bin_search(a,x,left,mid-1)
              
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

# Uses python3
import sys
import random
"""
algorithm
# choose pivot
swap a[n,rand(1,n)]

# 3-way partition
i = 1, k = 1, p = n
while i < p,
  if a[i] < a[n], swap a[i++,k++]
  else if a[i] == a[n], swap a[i,--p]
  else i++
end
→ invariant: a[p..n] all equal
→ invariant: a[1..k-1] < a[p..n] < a[k..p-1]

# move pivots to center
m = min(p-k,n-p+1)
swap a[k..k+m-1,n-m+1..n]

# recursive sorts
sort a[1..k-1]
sort a[n-p+k+1,n]
"""
def partition3(a, l, r):
    x = a[r]
    j = l-1;
    p = r;
    for i in range(l , r ):
        #print ("step" + str(i) )
        #print (a)
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i]==x and p>i:
            p =p-1           
            a[i], a[p] = a[p],a[i]
            if a[i] < x:
                j += 1
                a[i], a[j] = a[j], a[i]
     
    #print ("for loop over: step")
    #print (a)  
    y=min(r-p+1,p-j)
    
    #move pivot elements to the middle
    for i in range(y):
        a[r-i], a[j+1+i] = a[j+1+i], a[r-i]
    #print ("final list")
    #print (a)
    return j+1,r-p+j+1
    
    

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #print ("pivot")
    #print (k)
    a[r], a[k] = a[k], a[r]
    #m=partition2(a,l,r)
    #use partition3
    m1,m2= partition3(a, l, r)
    #print("m1")
    #print(m1)
    #print("m2")
    #print(m2)
    randomized_quick_sort(a, l, m1-1);
    randomized_quick_sort(a, m2 + 1, r);
    #randomized_quick_sort(a,l,m-1)
    #randomized_quick_sort(a,m+1,r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #input for stress test    
    #n=100000
    #a=[10]*n
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

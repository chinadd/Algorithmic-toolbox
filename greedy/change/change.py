# Uses python3

def get_change(n):
    #write your code here
    q1=0
    q2=0
    r1=0
    r2=0
    if (n >=10):
        q1=n//10
        r1=n%10
    else:
        r1=n
        
    if (r1 >=5):
        q2=r1//5
        r2=r1%5
    else:
        r2=r1
                
    return q1+q2+r2


n = int(input())
print(get_change(n))

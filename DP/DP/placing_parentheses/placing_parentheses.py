# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        
def MinMax(i,j,op,m,M):
    mini=10000
    maxi=-10000
    
    for k in range(i,j):
        a=int(evalt(M[i][k],M[k+1][j],op[k]))
        b=int(evalt(M[i][k],m[k+1][j],op[k]))
        c=int(evalt(m[i][k],M[k+1][j],op[k]))
        d=int(evalt(m[i][k],m[k+1][j],op[k]))
        mini=min(mini,a,b,c,d)
        maxi=max(maxi,a,b,c,d)
        
    return [mini,maxi]    
        
def get_maximum_value(dataset):
    #write your code here
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset)+1:2]
    n=int((len(dataset)+1)/2)
    #print(n)
    m=[[0 for x in range(n)] for x in range(n)]
    M=[[0 for x in range(n)] for x in range(n)]
    
    for i in range(n):
        m[i][i]=int(d[i])
        M[i][i]=int(d[i])
        
    #print (m)
    #print (M)
    
    for s in range(1,n):   #here's where I get confused
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i,j,op,m,M)   
    #print (m)
    #print (M)
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))

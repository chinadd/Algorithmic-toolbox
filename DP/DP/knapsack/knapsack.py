# Uses python3
import sys

        
def optimal_weight(W, w):
    # write your code here
    n=len(w)
    val = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):        
            if i==0 or j==0:
                val[i][j]=0
            elif w[i-1] <= j:
                val[i][j]=max(w[i-1]+val[i-1][j-w[i-1]],val[i-1][j])
            else:
                val[i][j]=val[i-1][j]    
    return val[n][j]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

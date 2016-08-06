# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)      
        s=[]
        m=0             
        x= n-1
        seq0 = list(optimal_sequence(x))      
        l = len(seq0)
        if n % 3 == 0:          
            y = n // 3            
            seq1 = list(optimal_sequence(y))
            if len(seq1)<l:
                m=1
                l=len(seq1)
        if n % 2 == 0:            
            z = n //2            
            seq2 = list(optimal_sequence(z))
            if len(seq2)<l:
                m=2
                l = len(seq2)  
                
        #print ("min index")
        #print (m)
        if m==0:
            n = x    
            #print ("n minus 1")
            #print (x)
        elif m==1:
            n = y
            #print ("n divide by 3")
            #print (y)
        elif m==2:
            n = z
            #print ("n divide by 2")
            #print (z)
            
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

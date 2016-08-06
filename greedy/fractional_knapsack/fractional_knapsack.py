# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    valueSum = 0
    # write your code here
    weightSum = 0
    
    if (len(weights)==1):
        if (capacity > weights[0]):
            valueSum=values[0]
        else:
            valueSum=values[0]*(float(capacity)/float(weights[0]))
    else:
        while (weightSum<=capacity and sum(weights)>0):
            i=0
            max_id=0
            max_num=0
            for i in range(len(weights)):           
                if (weights[i]>0 and float(values[i])/float(weights[i])>max_num):
                    max_num=float(values[i])/float(weights[i])
                    max_id=i
            #print (max_num)
            #print (max_id)
            
            if (float(weights[max_id])>0 and capacity-weightSum>0): 
                w= min(capacity-weightSum,weights[max_id])
                valueSum += w*(float(values[max_id])/float(weights[max_id]))
                #print (valueSum)
            
                values[max_id]-=w*(float(values[max_id])/float(weights[max_id]))
                weights[max_id]-=w
                #print (weights[max_id])
            
                weightSum += w
                #print (weight)
            else:
                #print ("finish")
                break
        
       
    return valueSum
#data = [int(x) for x in input().split()]

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

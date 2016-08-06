# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def addpoints(s,e):    
   p=[]
   for i in range(len(s)):
       if i==0:
           p.append(e[i])
       elif i>=1:
           if (s[i]>p[-1]):
               #p +=(addpoints(s[i:],e[i:]))
               p.append(e[i])
           else:
               m=min(p[-1],e[i])
               q=p[-1]
               p.remove(q)
               p.append(m)               
   return p

def optimal_points(segments):
    starts=[]
    ends=[]    
    #write your code here
    for s in segments:
        starts.append(s.start)
        ends.append(s.end)
       
    sortedends = [i[0] for i in sorted(zip(ends, starts), key=lambda l: l[1])]
    sortedstarts=[i[1] for i in sorted(zip(ends, starts), key=lambda l: l[1])]           
                           
    return addpoints(sortedstarts,sortedends)

if __name__ == '__main__':
    try:
        input = sys.stdin.read()
    except KeyboardInterrupt:
        pass
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

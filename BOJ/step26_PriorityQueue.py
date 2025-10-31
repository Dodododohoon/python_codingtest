#11279
import sys
from collections import deque

input=sys.stdin.readline

d = deque()
n=int(input())
max=0

for i in range(n):
    num = int(input())
    
    if num ==0:
        if not d:
            print('0')
        else:
            print(max)
            d.pop()
            if d:
                max=d[-1]
            else:
                max=0
    else:
         if num >= max:
             max = num
             d.append(num)
         else:
             d.appendleft(num)
         


#1927


#11286


#2075


#2696


#1202

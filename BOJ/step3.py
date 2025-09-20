#2739
"""
N = int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")
"""    
"""
#10950
n=int(input())
for i in range (n):
    A, B = map(int, input().split())
    print(A+B)
    """
#8393
#n = int(input())
#sum = 0
#for i in range(1,n+1):
#    sum += i   
#print(sum)
"""
#25304
total = int(input())
num = int(input())
sum =0
for i in range(num):
    A, B = map(int, input().split())
    sum = sum + A*B

if (total == sum):
    print("Yes")
else:
    print("No")
"""
#25314
#Byte =  int(input())
#num = Byte // 4
#for i in range(num):
#    print("long", end=' ')
#print("int")

#15552
#import sys

#N = int(sys.stdin.readline().rstrip())
#for i in range(N):
#    a, b= map(int, sys.stdin.readline().split())
#    print(f"{a+b}")


#11021
#N = int(input())
#for i in range(N):
#    a, b= map(int, input().split())
#    print(f"Case #{i+1}: {a+b}")

#11022
#import sys
#N = int(sys.stdin.readline().rstrip())

#for i in range(N):
#    a, b= map(int, sys.stdin.readline().split())
#    print(f"Case #{i+1}: {a} + {b} = {a+b}")

#2438
#num = int(input())
#for i in range(num):
#    for m in range(i+1):
#        print('*',end="")
#    print()
#for i in range(num):
#    print('*' * (i+1))

#2439
#num = int(input())
#for i in range(num):
#    print(' ' * (num-i-1), end="")
#    print('*' * (i+1))

#10952 -> while(True) 가능
#while(1): 
#    a, b = map(int, input().split())
#    if (a==0 and b==0):
#        break
#    print(a+b)

#10951
#import sys

#for line in sys.stdin:
#    a,b = map(int, line.split())
#    print(a+b)
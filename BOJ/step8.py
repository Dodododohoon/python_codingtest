#2745
#import sys

#li = sys.stdin.readline().split()
#num=[]
#result =0

#for ch in li[0]:
#    if ch.isdigit():                        # if '0' <= ch <= '9' 가능
#        num.append(int(ch))
#    else:
#        num.append(ord(ch)-55)

#trans = num[::-1]

#for i in range (len(trans)):
#    result += trans[i] * (int(li[1])**i)
#print(result)

#11005
#import sys

#num, B  = map(int, sys.stdin.readline().split())
#li=[]

#while(num//B):
#    if 0 <= num%B <= 9:
#        li.append(num%B)
#        num//=B
#    else:
#        li.append(chr(num%B+55))
#        num//=B

#if 0 <= num%B <= 9:
#    li.append(num%B)
#    num//=B
#else:
#    li.append(chr(num%B+55))
#            
#re=li[::-1]
#print(''.join(map(str, re)))

#2720                    #몫, 나머지 = divmod(a, b)  a / b
#n = int(input())

#for i in range(n):
#    num = int(input())
#    
#    num, cnt = divmod(num, 25)
#    print(num, end=' ')
#    
#    num, cnt = divmod(cnt, 10)
#    print(num, end=' ')
#    
#    num, cnt = divmod(cnt, 5)
#    print(num, end=' ')
#    print(cnt)

#2903
#n  = int(input())
#dot =2
#for i in range(n):
#    dot = dot + (dot-1)
#print(dot**2)

#2292
#n= int(input())

#num=1
#cnt=1
#while(n>num):
#    num=num+6*cnt
#    cnt+=1
#print(cnt)


#1193
#n = int(input())

#k=0
#total=0
#while(n>total):
#    k+=1
#    total = (k*(k+1))/2
#num = int(n - (k*(k-1))/2)

#if(k%2==0):
#    print(f"{num}/{k-num+1}")
#if(k%2==1):
#    print(f"{k-num+1}/{num}")

#2869
import sys

a, b, v = map(int, sys.stdin.readline().split())
#day=0
#total =0
day = (v-a)/(a-b)
num = (v-a)%(a-b)

if day ==0:
    print('1')
elif(num==0):
    print(int(day) +1)
else:    
    day = int(day) +1
    print(day+1)

#while(v>total):
#    day +=1
#    total = a*day - b*day + a
#print(day+1)
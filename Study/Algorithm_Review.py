##BackTracking

#15649 - 바로 안 떠올랐음.
#import sys
#sys.setrecursionlimit(10**6)

#input = sys.stdin.readline

#n, m = map(int, input().split())
#visited = [False] * (n+1)
#arr=[]

#def BT(num):
#    if num == m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(1,n+1):
#        if visited[i] == False:
#            visited[i] = True
#            arr.append(i)
#            BT(num+1)
#            arr.pop()
#            visited[i] = False
#            
#BT(0)

#15650
#import sys
#input = sys.stdin.readline

#n, m = map(int, input().split())

#arr=[]

#def bt(k):
#    if len(arr) == m:
#        print(' '.join(map(str, arr)))
#        return
#    for i in range(k,n+1):
#        arr.append(i)
#        bt(i+1)
#        arr.pop()
#                    
#bt(1) 
#---------------------------------------------------------
##Dynamic Programming
#2579
#import sys

#input = sys.stdin.readline
#n = int(input())
#arr = [int(input()) for _ in range(n)]
#arr.insert(0,0)

#if n ==1:
#    print(arr[1])
#    exit()
#if n==2:
#    print(arr[1]+arr[2])
#    exit()

#dp = [0] * (n+1)
#dp[1] = arr[1]
#dp[2] = arr[1]+arr[2]


#for i in range(3, n+1):
#    dp[i] = max(dp[i-2], dp[i-3]+arr[i-1]) + arr[i]

#print(dp[n])
#--------------------------------------------------
##Prefix Sum
#11659
#import sys
#input = sys.stdin.readline

#n,m = map(int, input().split())

#li = list(map(int, input().split()))

#prefix = [0] * (n+1)

#for i in range(1,n+1):
#    prefix[i] = prefix[i-1] + li[i-1]

#for _ in range(m):
#    i, j =map(int, input().split())
#    print(prefix[j] - prefix[i-1])
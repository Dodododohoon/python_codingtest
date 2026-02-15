#2240 자두나무
#import sys
#input =sys.stdin.readline

#t,w = map(int,input().split())

#arr = [int(input()) for _ in range(t)]

#dp=[[0] * (w+1) for _ in range(t+1)]

#for i in range(1,t+1):
#    for j in range(0,w+1):
#        if arr[i-1] == 1:
#            if j ==0:
#                dp[i][j] = dp[i-1][j] +1
#            elif j % 2 ==0:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
#            else:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
#        else:
#            if j % 2 ==1:
#                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
#            elif j ==0:
#                dp[i][j] = dp[i-1][j]
#            else:
#                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
#            

#print(max(dp[t]))
#9095
#import sys
#input = sys.stdin.readline

#t = int(input())

#dp = [0] * 11
#dp[0] = 1
#dp[1] = 1
#dp[2] = 2
#for i in range(3,11):
#    dp[i] = dp[i-1] + dp[i-2] +dp[i-3]

#for _ in range(t):
#    n = int(input())
#    print(dp[n])

#1697 - 시작값 에러 있음. & 더 짧게 가능.
#import sys
#from collections import deque

#n, k = map(int, input().split())
#time = [0] * 100001

#q = deque([(0,n)])

#while q:
#    t, loc = q.popleft()
#    
#    if loc == k:
#        break
#    
#    nx = 2*loc
#    if 0 <= nx <= 100000 and time[nx] == 0:
#        time[nx] = t+1
#        q.append((t+1,nx))
#        
#    nx = loc +1
#    if 0 <= nx <= 100000 and time[nx] ==0:
#        time[nx] = t+1
#        q.append((t+1,nx))
#        
#    nx = loc -1
#    if 0 <= nx <= 100000 and time[nx] == 0:
#        time[nx] = t+1
#        q.append((t+1,nx))

#print(time[k])

#2293
#import sys
#input = sys.stdin.readline

#n,k = map(int, input().split())
#coins = [int(input()) for _ in range(n)]
#dp = [0] * 10001
#dp[0] = 1

#for coin in coins:
#    for i in range(coin, k+1):
#        dp[i] += dp[i-coin] 

#print(dp[k])

#11052
#import sys
#input = sys.stdin.readline

#n = int(input())
#arr = list(map(int,input().split()))

#dp = [0]*(n+1)
#dp[1] = arr[0]

#dp[2] = max(dp[1]+arr[0], arr[1])

#for i in range(3,n+1):
#    for j in range(i):
#        dp[i] = max(dp[i], dp[j] + arr[i-j-1])

#print(dp[n])

#2225
#import sys
#input = sys.stdin.readline

#n,k = map(int,input().split())

#dp = [[0] * (k+1) for _ in range(n+1)]

#for i in range(1,k+1):
#    dp[0][i] = 1
#for i in range(1,n+1):
#    dp[i][1] = 1

#for i in range(1,n+1):
#    for j in range(2,k+1):
#        for m in range(i+1):
#            dp[i][j] += dp[m][j-1] % 1000000000
#print(dp[n][k]%1000000000)

#1309
#import sys
#input = sys.stdin.readline

#n = int(input())

#dp = [0] * (n+1)
#dp[0] = 1
#dp[1] = 3

#for i in range(2, n+1):
#    dp[i] = (2* dp[i-1] + dp[i-2])%9901 
#print(dp[n]%9901)

#9184
#import sys
#input = sys.stdin.readline

#dp =[[[0]*21 for _ in range(21)] for _ in range(21)]

#for i in range(21):
#    for j in range(21):
#        for m in range(21):
#            if i == 0 or j ==0 or m == 0:
#                dp[i][j][m] = 1
#                continue
#            if i<j<m:
#                dp[i][j][m] = dp[i][j][m-1] +dp[i][j-1][m-1] - dp[i][j-1][m]
#            else:
#                dp[i][j][m] = dp[i-1][j][m] + dp[i-1][j-1][m]+dp[i-1][j][m-1]-dp[i-1][j-1][m-1]

#while True:
#    a,b,c = map(int,input().split())
#    if a==-1 and b==-1 and c==-1:
#        break
#    if a <= 0 or b <= 0 or c <= 0:
#        print(f'w({a}, {b}, {c}) = {dp[0][0][0]}')
#        continue
#    if a >20 or b >20 or c > 20:
#        print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
#    else:
#        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')
    
#1012
#import sys
#from collections import deque
#input =sys.stdin.readline

#t = int(input())

#for _ in range(t):
#    m,n,k = map(int,input().split())
#    
#    graph = [[0] * m for _ in range(n)]
#    cnt = 1
#    dx = [1,-1,0,0]
#    dy = [0,0,1,-1]
#    
#    for _ in range(k):
#        x, y = map(int,input().split())
#        
#        graph[y][x] = 1
# 
#    def bfs(a,b,c):
#        q=deque([(a,b)])
#        while q:
#            y, x = q.popleft()
#            
#            for i in range(4):
#                nx = x + dx[i]
#                ny = y + dy[i]
#                
#                if 0<=nx<m and 0<=ny<n and graph[ny][nx] ==1:
#                    graph[ny][nx] = c
#                    q.append((ny,nx))
#        
#    for i in range(n):
#            for j in range(m):
#                if graph[i][j] == 1:
#                    cnt +=1
#                    graph[i][j] = cnt
#                    bfs(i,j,cnt)
#        
#    print(cnt-1)
        
        
        
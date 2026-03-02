#2178
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]
score = [[10000]*m for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(row, col):
  for i in range(4):
    nr = row + dr[i]
    nc = col + dc[i]

    if 0<= nr < n and 0<= nc <m and graph[nr][nc] == 1:
      graph[nr][nc]=2
      score[nr][nc]=min(score[nr][nc], score[row][col] + 1)
      if nr ==n-1 and nc ==m-1:
        print(score[n-1][m-1])
        exit()
      dfs(nr,nc)
      graph[nr][nc]=1


graph[0][0]=2
score[0][0]=1
dfs(0,0)
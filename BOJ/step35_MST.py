
#9372
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#t = int(input())    

#for _ in range(t):
#    n,m = map(int,input().split())
#    graph = [ [] for _ in range(n+1)]
#    visited = [False] * (n+1)
#    cnt = 0
#    
#    def dfs(v):
#        global cnt
#        visited[v] = True
#        
#        for u in graph[v]:
#            if visited[u] == False:
#                cnt += 1
#                dfs(u)
#     
#    for _ in range(m):
#        a,b = map(int, input().split())
#        graph[a].append(b)
#        graph[b].append(a)
#    
#    dfs(1)
#    print(cnt)

#1197
import sys
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
parents = [i for i in range(v+1)]
rank = [0] * (v+1)

def find(a):
    if parents[a] != a:
        return find(parents[a])
    return parents[a]
    
def union(a,b):
    a= find(a)
    b= find(b)
    
    if rank[a] < rank[b]:
        parents[a] = b
    else:
        if rank[a] == rank[b]



for _ in range(e):
    a,b,c = map(int,input().split())
    edge.append((a,b,c))

edge = sorted(edge, key=lambda x: x[2])
cnt=0
score =0


#4386


#1774


#6497


#17472


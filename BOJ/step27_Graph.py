#그래프 : 정점(Vertex)과 간선(Edge)로 이루어진 자료구조.
#DFS : Depth First Search. 깊이 우선 탐색. 한 경로를 끝까지 탐색한 후, 다음 경로
#BFS : Breadth First Search. 너비 우선 탐색. 현재 정점에서 가까운 노드부터 탐색 


#24479
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#n,m,r = map(int, input().split())

#node = [[] for _ in range(n+1)]
#visited = [0] *(n+1)

#for _ in range(m):
#    a,b = map(int, input().split())
#    node[a].append(b)
#    node[b].append(a)

#for i in range(1,n+1):
#    node[i].sort()

#cnt = 0

#def dfs(r):
#    global cnt
#    cnt+=1
#    visited[r] = cnt
#    
#    for x in node[r]:
#        if visited[x] == 0:
#            dfs(x)
#    return

#dfs(r)
#print('\n'.join(map(str, visited[1:])))
             
#24480
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

#n, m, r = map(int, input().split())

#visited = [0]*(n+1)
#graph = [[] for _ in range(n+1)]

#for _ in range(m):
#    a, b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)

#for i in range(1,n+1):
#    graph[i].sort(reverse=True)

#cnt =0

#def dfs(r):
#    global cnt
#    cnt+=1
#    visited[r] = cnt
#    
#    for x in graph[r]:
#        if visited[x] == 0:
#            dfs(x)
#    return
#dfs(r)

#print('\n'.join(map(str, visited[1:])))
    

#24444

#24445

#2606

#1260

#2667

#1012

#2178

#7562

#7576

#7569

#16928

#2206

#1707
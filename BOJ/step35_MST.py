# 9372
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
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

# 1197
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# v, e = map(int, input().split())

# parents = [i for i in range(v + 1)]
# edge = []


# def find(a):
#     if parents[a] != a:
#         parents[a] = find(parents[a])
#     return parents[a]


# def union(a, b):
#     a = find(a)
#     b = find(b)

#     if a != b:
#         parents[b] = a


# for _ in range(e):
#     a, b, c = map(int, input().split())
#     edge.append((a, b, c))

# edge = sorted(edge, key=lambda x: x[2])
# ans = 0
# cnt = 0

# for a, b, c in edge:
#     if find(a) != find(b):
#         union(a, b)
#         ans += c
#         cnt += 1
#     if cnt == v - 1:
#         break

# print(ans)

# 처음에 그냥 dfs로 풀다가 알고보니 에러 있어서 유니온 파인드로 다시 풀었음.
# 그런데 유니온 파인드 기억이 잘 안나서 find, union 함수는 조금 보면서 풀었음.

# 4386


# 1774


# 6497


# 17472

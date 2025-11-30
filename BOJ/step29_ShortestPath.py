# - 가중치 없음 → BFS
# - 모든 가중치 양수 → 다익스트라
# - 음수 가중치 존재 → 벨만–포드
# - 모든 정점 쌍 거리 필요 → 플로이드–워셜
# - SPFA는 사용 권장 X (최악 시간 때문에)

# 1753 - 다익스트라
# import sys
# import heapq

# input = sys.stdin.readline

# v, e = map(int, input().split())
# k = int(input())

# graph = [[] for _ in range(v+1)]

# INF = int(1e9)
# dist = [INF] * (v+1)
# dist[k] = 0

# for _ in range(e):
#    a,b,c = map(int, input().split())
#    graph[a].append((b,c))

# hq = []
# heapq.heappush(hq, (0,k))

# while hq:
#    cur_dist, u = heapq.heappop(hq)
#
#    if cur_dist > dist[u]:
#        continue
#
#    for nxt, w in graph[u]:
#        nd = cur_dist + w
#        if nd < dist[nxt]:
#            dist[nxt] = nd
#            heapq.heappush(hq, (nd, nxt))         #lazy deletion
#
# for i in range(1,v+1):
#    if dist[i] ==INF:
#        print('INF')
#    else:
#        print(dist[i])

# 1504
# import sys
# import heapq

# input = sys.stdin.readline

# n,e = map(int, input().split())

# INF = int(1e9)

# graph = [[] for _ in range(n+1)]
# dist_a = [INF] * (n+1)
# dist_b = [INF] * (n+1)
# dist_c = [INF] * (n+1)
# dist_a[1] = 0

# for _ in range (e):
#    a,b,c = map(int, input().split())
#    graph[a].append((b,c))
#    graph[b].append((a,c))
#
# v1,v2 = map(int,input().split())

# dist_b[v1] = 0
# dist_c[v2] = 0

# hq = [(0,1)]

# while hq:
#    cur_dist, u = heapq.heappop(hq)
#
#    if cur_dist > dist_a[u]:
#        continue
#
#    for nxt, w in graph[u]:
#        nd = cur_dist + w
#        if dist_a[nxt] > nd:
#            dist_a[nxt] = nd
#            heapq.heappush(hq, (nd,nxt))

# hq = [(0,v1)]

# while hq:
#    cur_dist, u = heapq.heappop(hq)
#
#    if cur_dist > dist_b[u]:
#        continue
#
#    for nxt, w in graph[u]:
#        nd = cur_dist + w
#        if dist_b[nxt] > nd:
#            dist_b[nxt] = nd
#            heapq.heappush(hq, (nd,nxt))


# hq = [(0,v2)]

# while hq:
#    cur_dist, u = heapq.heappop(hq)
#
#    if cur_dist > dist_c[u]:
#        continue
#
#    for nxt, w in graph[u]:
#        nd = cur_dist + w
#        if dist_c[nxt] > nd:
#            dist_c[nxt] = nd
#            heapq.heappush(hq, (nd,nxt))

# ans1 = dist_a[v1] + dist_b[v2] +dist_c[n]
# ans2 = dist_a[v2] + dist_c[v1] +dist_b[n]
# k = min(ans1,ans2)

# if k >= INF:
#    print('-1')
# else:
#    print(k)

# 오~~!!! 꽤 빡센거 같은데 Self로 풀었음.
# 약간 구조가 길어져서 설마 이거 일까 했는데 맞음.
# 다익스트라 세번 돌렸는데 그냥 함수로 만들어서 3번 돌리는게 깔끔.

# 13549
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, k = map(int, input().split())


# 9370


# 11657


# 11404


# 1956


# memo

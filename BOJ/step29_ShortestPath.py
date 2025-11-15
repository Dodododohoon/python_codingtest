#- 가중치 없음 → BFS
#- 모든 가중치 양수 → 다익스트라
#- 음수 가중치 존재 → 벨만–포드
#- 모든 정점 쌍 거리 필요 → 플로이드–워셜
#- SPFA는 사용 권장 X (최악 시간 때문에)

#1753 - 다익스트라
#import sys
#import heapq

#input = sys.stdin.readline

#v, e = map(int, input().split())
#k = int(input())

#graph = [[] for _ in range(v+1)]

#INF = int(1e9)
#dist = [INF] * (v+1)
#dist[k] = 0

#for _ in range(e):
#    a,b,c = map(int, input().split())
#    graph[a].append((b,c))

#hq = []    
#heapq.heappush(hq, (0,k))

#while hq:
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
#for i in range(1,v+1):
#    if dist[i] ==INF:
#        print('INF')
#    else:
#        print(dist[i])



#1504


#13549


#9370


#11657


#11404


#1956


#우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# heapq 이용. 파이썬에서는 min heap이 기본 구조.

#11279
#import sys
#import heapq

#input=sys.stdin.readline

#n = int(input())

#heap = []    

#for _ in range(n):
#    x = int(input())
#    
#    if x:
#        heapq.heappush(heap,-x)
#    else:
#        if heap:
#            k = heapq.heappop(heap)
#            print(-k)
#        else:
#            print('0')
        

#1927
#import sys
#import heapq

#input=sys.stdin.readline

#n = int(input())

#heap = []    
#for _ in range(n):
#    x = int(input())
#    
#    if x:
#        heapq.heappush(heap,x)
#    else:
#        if heap:
#            print(heapq.heappop(heap))
#        else:
#            print('0') 

#11286
#import sys
#import heapq

#input = sys.stdin.readline

#heap =[]
#n = int(input())

#for _ in range(n):
#    x = int(input())
#    
#    if x == 0:
#        if heap:
#            print(heapq.heappop(heap)[1])
#        else:
#            print('0')
#    else:
#        heapq.heappush(heap,(abs(x),x))
        

#2075
#import heapq
#import sys

#input = sys.stdin.readline

#n = int(input())
#h = list(map(int, input().split()))
#heapq.heapify(h)

#----------------------------------- 내 풀이.
#for _ in range(n-1):
#    tmp = [-x for x in map(int, input().split())]
#    heapq.heapify(tmp)
#    
#    while -(tmp[0]) > h[0]:
#        a = -heapq.heappop(tmp)
#        heapq.heappop(h)
#        heapq.heappush(h,a)
#------------------------------------ 더 심플 버전
#for _ in range(n-1):
#    for x in map(int, input().split()):
#        if x >h[0]:
#            heapq.heapreplace(h,x)


#print(h[0])

#2696


#1202

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

#2696                    꼭 다시 풀어보자.
#import sys
#import heapq
#input= sys.stdin.readline

#t = int(input())
#arr=[]

#for _ in range(t):
#    arr=[]
#    m = int(input())
#    for _ in range((m+9)//10):
#        arr.extend(map(int,input().split()))
#    
#    out = []
#    left = []
#    right = []
#    
#    for i in range(m):
#        if not left or arr[i] <= -left[0]:
#            heapq.heappush(left, -arr[i])
#        else:
#            heapq.heappush(right, arr[i]) 
#    
#        if len(left) > len(right) +1 :
#            heapq.heappush(right, -heapq.heappop(left))
#        elif len(left) < len(right):
#            heapq.heappush(left, -heapq.heappop(right))
#            
#        if i % 2 ==0:
#            out.append(-left[0])
#        
#    print((m+1)//2)
#    for i in range(len(out)):
#        if i != 0 and i % 10 ==0:
#            print('')
#        print(out[i], end=' ')



#for _ in range(t):                나의 쓰레기 같은 풀이. BUT 온몸비틀기는 했다 ^^
#    m = int(input())
#    k = (m-1) // 10
#    for i in range(k+1):
#        temp = list(map(int, input().split()))
#        arr = arr + temp
#    h1=[]
#    h2=[]
#    
#    for i in range(m):
#        heapq.heappush(h1, arr[i])
#        if i%2 ==0:
#            if i != 0 and i % 18 ==0:
#                print('')
#            h2 = list(h1)
#            cnt = i
#            while h1:
#                if cnt == i//2:
#                    print(heapq.heappop(h1), end= ' ')
#                    cnt -= 1
#                    continue
#                heapq.heappop(h1)
#                cnt -= 1
#            h1 = list(h2)

#1202

#---------------Review------------------
#11286                        gpt기준 이게 더 가독성이 좋다고 하긴 하는데 abs로 푸는 방법도 있음.

#import sys
#import heapq
#input = sys.stdin.readline

#n = int(input())
#------abs사용 힙큐 하나 풀이
#h = []

#for _ in range(n):
#    x = int(input())
#    
#    if x != 0:
#        heapq.heappush(h,(abs(x), x))
#    else:
#        if h:
#            a,b = heapq.heappop(h)
#            print(b)
#        else:
#            print('0')
#-----마이너스 플러스 분리 풀이
#hm = []
#hp = []

#for _ in range(n):
#    num = int(input())
#    
#    if num == 0:
#        if not hm and not hp:
#            print('0')
#        elif not hm and hp:
#            print(heapq.heappop(hp))
#        elif not hp and hm:
#            print(-(heapq.heappop(hm)))
#        else:
#            if hm[0] > hp[0]:
#                print(heapq.heappop(hp))
#            else:
#                print(-(heapq.heappop(hm)))          
#                
#    elif num<0:
#        heapq.heappush(hm,-(num))
#    else:
#        heapq.heappush(hp,num)
        
    



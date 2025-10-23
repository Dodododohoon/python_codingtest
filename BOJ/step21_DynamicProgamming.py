#동적 계획법 핵심은 중복되는 계산은 기억해두고 푼다.
# 메모리를 사용해서 연산을 줄인다.

#24416    
#n = int(input())

#if n==1 or n==2:
#    print(1,0)
#else:
#    f1, f2 =1, 1
#    for _ in range(3, n+1):
#        f1 ,f2 = f2, f2+ f1
#    print(f2, n-2)

#9184
#import sys
#input = sys.stdin.readline

#cache ={}

#def w(a,b,c):
#    if a<= 0 or b <= 0 or c <= 0:
#        return 1
#    elif a> 20 or b>20 or c>20:
#        return w(20,20,20)
#    elif (a,b,c) in cache:
#        return cache[(a,b,c)]
#    
#    if a < b< c :
#        cache[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
#    else:
#        cache[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) +w(a-1,b,c-1) - w(a-1,b-1,c-1)
#    return cache[(a,b,c)]

#for line in sys.stdin:
#    a,b,c = map(int, line.split())
#    if a==-1 and b==-1 and c==-1:
#        break
#    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
    
#동적계획법 거의 첫 문제. 

#1904
#import sys
#input = sys.stdin.readline

#n = int(input())

#memo = {}
#memo[1] = 1
#memo[2] = 2
#    
#for i in range (3,n+1):
#    memo[i] = (memo[i-1]+memo[i-2])%15746
#    
#print(memo[n])
#-------============밑에 recusionError    
#def dp(n):
#    global memo
#    if n in memo:
#        return memo[n]
#    else:
#        memo[n] = dp(n-1) +dp(n-2)
#        return memo[n]
#        
#print(dp(n)%15746)

#딕셔너리 그냥 리스트 써도 상관없음
#처음에 재귀 형태로 썼다가 for 문으로 바텀업 DP하니깐 클리어

#9461

#1912

#1149

#1932

#2579

#1463

#10844

#2156

#11053

#11054

#2565

#9251

#12865

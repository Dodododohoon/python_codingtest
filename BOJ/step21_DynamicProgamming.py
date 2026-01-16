# 동적 계획법 핵심은 중복되는 계산은 기억해두고 푼다.
# 메모리를 사용해서 연산을 줄인다.

# 24416
# n = int(input())

# if n==1 or n==2:
#    print(1,0)
# else:
#    f1, f2 =1, 1
#    for _ in range(3, n+1):
#        f1 ,f2 = f2, f2+ f1
#    print(f2, n-2)

# 9184
# import sys
# input = sys.stdin.readline

# cache ={}

# def w(a,b,c):
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

# for line in sys.stdin:
#    a,b,c = map(int, line.split())
#    if a==-1 and b==-1 and c==-1:
#        break
#    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

# 동적계획법 거의 첫 문제.

# 1904
# import sys
# input = sys.stdin.readline

# n = int(input())

# memo = {}
# memo[1] = 1
# memo[2] = 2
#
# for i in range (3,n+1):
#    memo[i] = (memo[i-1]+memo[i-2])%15746
#
# print(memo[n])
# -------============밑에 recusionError
# def dp(n):
#    global memo
#    if n in memo:
#        return memo[n]
#    else:
#        memo[n] = dp(n-1) +dp(n-2)
#        return memo[n]
#
# print(dp(n)%15746)

# 딕셔너리 그냥 리스트 써도 상관없음
# 처음에 재귀 형태로 썼다가 for 문으로 바텀업 DP하니깐 클리어

# 9461
# import sys

# input = sys.stdin.readline

# pn = [1, 1, 1, 2, 2]

# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if num > len(pn):
#         for i in range(len(pn), num):
#             pn.append(pn[i - 1] + pn[i - 5])
#     print(pn[num - 1])

# 1912
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0 for _ in range(n)]
# dp[0] = arr[0]

# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i - 1] + arr[i])

# print(max(dp))

# 아.. 풀만했는데 아 .. 종이 있었으면 나앗을라나?
# 점화식만 뽑아내면 어렵지 않음.

# 1149
# import sys
# input = sys.stdin.readline

# n= int(input())

# a,b,c = map(int, input().split())

# for _ in range(n-1):
#    p,q,r = map(int, input().split())
#
#    s1 = p + min(b,c)
#    s2 = q +min(a,c)
#    s3 = r + min(a,b)
#
#    a, b,c = s1,s2,s3
#
# print(min(a,b,c))

# DP 테이블을 만들 수 있음.
# dp[i][0] = R[i] + min(dp[i-1][1], dp[i-1][2]) 이런식으로

# 내께 메모리도 아껴서 더 좋긴한데 난 학습하고 있으니. 테이블 쓰려고 해보자.

# 1932
# import sys
# input = sys.stdin.readline

# n=int(input())

# li=[list(map(int, input().split())) for _ in range(n)]
# dp = li[:]

# for i in range(0, n):
#    if i ==0:
#        continue
#    for j in range(i+1):
#        if j==0:
#            dp[i][0] = li[i][0] + li[i-1][0]
#        elif j==i:
#            dp[i][j] = li[i][j] + li[i-1][j-1]
#        else:
#            dp[i][j] = li[i][j] + max(li[i-1][j-1], li[i-1][j])

# print(max(dp[n-1]))

# dp = li[:] 이부분 자칫하다간 틀릴뻔 했음. (얕은 복사)
# 내가 우려했던대로 같은 값을 가르키고 있는게 맞네? append로 해서 다르게 출력되길레 다르구나 했는데. append해서 추가된 값은 따로고
# 기존 내부 값들은 똑같이 가르키고 있대.
# li나 dp 수정하면 같이 바뀌는거지.

# 깊은 복사 하려면. dp = [x[:] for x in li] 이렇게 해야함.

# 2579
# import sys

# input = sys.stdin.readline

# n = int(input())

# arr = [int(input()) for _ in range(n)]
# arr.insert(0, 0)

# dp = [0 for _ in range(n + 1)]


# if n >= 4:
#    dp[1] = arr[1]
#    dp[2] = arr[2] + arr[1]
#    dp[3] = max(arr[1], arr[2]) + arr[3]

#    for i in range(4, n + 1):
#        dp[i] = max(dp[i - 2], arr[i - 1] + dp[i - 3]) + arr[i]
#    print(dp[n])

# elif n == 1:
#    print(arr[1])
# elif n == 2:
#    print(arr[1] + arr[2])
# elif n == 3:
#    print(max(arr[1], arr[2]) + arr[3])

# 1463
# n = int(input())
# dp = [0] * (n+1)

# for i in range(2, n+1):
#        dp[i] = dp[i-1] +1
#        if i%2==0:
#            dp[i] = min(dp[i], dp[i//2]+1)
#        if i%3==0:
#            dp[i] = min(dp[i], dp[i//3]+1 )
#
# print(dp[n])

# 아쉽네, 뭔가 풀 수 있었을 거 같은데.. 너무 빨리 포기했나 싶기도?
# 점화식만 뽑아내면 아무 어려운거 없는 문제

# 10844
# n = int(input())
# dp = [[1]*10 for _ in range((n+1))]
# dp[1][0] = 0

# for i in range(2,n+1):
#    for j in range(1, 9):
#        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#    dp[i][0] = dp[i-1][1]
#    dp[i][9] = dp[i-1][8]
#
# print(sum(dp[n])%1000000000)

# 하.. 규칙은 잘 찾았는데 2차원으로 풀어야 할 줄은 몰랐네.. ㄹㅇ 까비.
# BUT 하나 배웠음. 애매하게 풀 바에 메모리 낭비좀 하더라도 2차원 적극 쓰자.

# 2156
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = [int(input()) for _ in range(n)]
# li.insert(0, 0)

# dp = [0] * (n + 1)

# if n >= 4:
#     dp[1] = li[1]
#     dp[2] = li[1] + li[2]
#     dp[3] = max(dp[1] + li[3], dp[2], li[2] + li[3])
#     for i in range(4, n + 1):
#         dp[i] = max(dp[i - 2] + li[i], dp[i - 3] + li[i - 1] + li[i], dp[i - 1])
#     print(max(dp[n], dp[n - 1]))
# elif n == 1:
#     print(li[1])
# elif n == 2:
#     print(li[1] + li[2])
# elif n == 3:
#     dp[1] = li[1]
#     dp[2] = li[1] + li[2]
#     dp[3] = max(dp[1] + li[3], dp[2], li[2] + li[3])
#     print(dp[3])

# 반례를 찾아서 내가 틀렸다는 건 알겠는데, 정확하게 왜 틀렸는지는 이해가 안감..
# 약간 찜찜하긴 했는데

# 11053
# import sys
# input = sys.stdin.readline

# n= int(input())
# li = list(map(int, input().split()))

# dp = [1] * (n)

# for i in range(1,n):
#    dp_max=0
#    for j in range(0,i):
#        if li[i] > li[j] and dp_max < dp[j]:
#            dp_max = dp[j]
#    dp[i] = dp_max + 1
#
# print(max(dp))

# 점화식 뽑아내는게 힘들어서 힌트 받음..

# 11053
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# dp = [1] * (n)

# for i in range(1,n):
#    dp_max = 0
#    for j in range(0,i):
#        if arr[i] > arr[j] and dp_max < dp[j]:
#            dp_max = dp[j]
#    dp[i] = dp_max +1

# print(max(dp))


# 11054                    나름 혼자 풀 수도 있었는데 까비. 반례만 빨리 찾았어도. 직접 풀었을 듯.
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr =list(map(int,input().split()))

# dp_up = [1] * n
# dp_down = [1] * n

# for i in range(1,n):
#    dp_max = 0
#    for j in range(0,i):
#        if arr[i] > arr[j] and dp_max < dp_up[j]:
#            dp_max = dp_up[j]
#    dp_up[i] = dp_max +1

# change = dp_up.index(max(dp_up))

# for i in range(n-1,-1,-1):
#    dp_max = 0
#    for j in range(n-1,i,-1):
#        if arr[i] > arr[j] and dp_max < dp_down[j]:
#            dp_max = dp_down[j]
#    dp_down[i] = dp_max + 1
# ans = 0

# for i in range(n):
#    ans = max(ans,(dp_up[i] + dp_down[i] -1))
# print(ans)

# 2565
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = []

# for _ in range(n):
#     a, b = map(int, input().split())

#     arr.append((a, b))
# arr.sort()

# dp = [1] * n

# for i in range(1, n):
#     max_dp = 0
#     for j in range(0, i):
#         if arr[i][1] > arr[j][1] and max_dp < dp[j]:
#             max_dp = dp[j]
#     dp[i] = max_dp + 1

# print(n - max(dp))

# 9251

# 12865

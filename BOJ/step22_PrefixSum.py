# 배열의 특정 구간 i~j의 합을 빠르게 구하는 문제.
# 매번 sum()으로 더하면 시간초과 나므로,
# 누적합(prefix sum) 으로 미리 더해두고 한 번에 처리!

# 11659
# import sys
# input=sys.stdin.readline

# n,m = map(int, input().split())

# li = list(map(int, input().split()))

# prefix = [0] * (n+1)
# prefix_sum=0
# for i in range(1,n+1):
#    prefix[i] = prefix[i-1] +li[i-1]

# for _ in range(m):
#    i, j = map(int, input().split())
#    prefix_sum = prefix[j] - prefix[i-1]
#    print(prefix_sum)

# 2559
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# li = list(map(int, input().split()))
# prefix = [0]*(n+1)

# for i in range(1,n+1):
#    prefix[i] = prefix[i-1] + li[i-1]

# prefix_sum = [0] * (n+1)

# for i in range(k,n+1):
#    prefix_sum[i] = prefix[i]-prefix[i-k]

# print(max(prefix_sum[k:]))
# print(max(prefix[i] - prefix[i - k] for i in range(k, n + 1)))


# 초기값 =0 이라서 최대가 음수인 경우에 틀렸다고 하더라.
# 출력방법 2가지. but 2번째 방식 꽤 신박하네
# 제네레이터 표현식이라고 하네. 적응하면 꽤나 유용할 거 같은데 일단 keep

# 16139
# import sys
# input = sys.stdin.readline

# s = input().strip()
# n = int(input())
#
# pre = [[0]*26 for _ in range(len(s)+1)]
# for i in range(1, len(s)+1):
#    for j in range(26):
#        if ord(s[i-1]) - 97 == j:
#            pre[i][j] = pre[i-1][j] +1
#        else:
#            pre[i][j] = pre[i-1][j]
#
# for i in range(1, len(s)+1):
#    for j in range(26):
#        pre[i][j] = pre[i-1][j]
#    pre[i][ord(s[i-1])-97] +=1

# for _ in range(n):
#    le, l, r = map(str, input().split())
#    l, r = int(l), int(r)
#    re =ord(le) -97
#    print(pre[r+1][re] - pre[l][re])


########밑에는 a에 우선 적용##
# pre_a = [0] * (len(s)+1)

# for i in range(1,len(s)+1):
#    if s[i-1] == 'a':
#        pre_a[i]=pre_a[i-1] + 1
#    else:
#        pre_a[i]=pre_a[i-1]

# for _ in range(n):
#    le, l, r = map(str, input().split())
#    if le =='a':
#        print(pre_a[int(r)+1] - pre_a[int(l)])

# 10986
# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# li = list(map(int, input().split()))
# dic = dict()

# prefix = [0] * (n+1)
# for i in range(1,n +1):
#    k = (prefix[i-1] + li[i-1]) % m
#    prefix[i] = k
#    if k in dic:
#        dic[k] +=1
#    else:
#        dic[k] = 1
# cnt=0

# for x in dic:
#    r = dic[x]
#    if x == 0:
#        cnt += r*(r+1)//2
#    else:
#        cnt += r*(r-1)//2

# 구간 나머지에서 구간합 자체를 나머지로 받는거 까진 생각했는데
# S[i] - S[j] =0 이걸 생각을 못했음. 이 아이디어만 좀 빌리고 구현은 직접함.

# print(cnt)

# 11660
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# li = [list(map(int, input().split())) for _ in range(n)]

# prefix = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         prefix[i][j] = prefix[i][j - 1] + li[i - 1][j - 1]

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     sum = 0
#     for i in range(x1, x2 + 1):
#         sum += prefix[i][y2] - prefix[i][y1 - 1]
#     print(sum)

# 25682


# --------------REVIEW-----------
# 2559
# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())

# arr = list(map(int, input().split()))

# pre = [0] * (n + 1)
# sum = -1000000000

# for i in range(1, n + 1):
#     pre[i] = pre[i - 1] + arr[i - 1]

# for i in range(k, n + 1):
#     sum = max(sum, pre[i] - pre[i - k])

# print(sum)

#10986
#import sys
#input = sys.stdin.readline

#n,m = map(int,input().split())
#arr = list(map(int,input().split()))

#prefix = [0] * (n+1)
#c = [0] * (m)
#cnt = 0

#for i in range(1,n+1):
#    prefix[i] = (prefix[i-1] + arr[i-1]) % m 

#for i in range(1,n+1):
#    if prefix[i] ==0:
#        c[0] += 1
#        cnt += c[0]
#    else:
#        c[prefix[i]] +=1
#        cnt += c[prefix[i]] - 1

#print(cnt)
    
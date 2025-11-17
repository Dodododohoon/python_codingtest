# 27433
# def fect(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return fect(x - 1) * x

# n = int(input())

# print(fect(n))


# 10870
# def pibo(x):
#    if x == 0:
#        return 0
#    elif x == 1:
#        return 1
#    else:
#        return pibo(x - 1) + pibo(x - 2)


# n = int(input())
# print(pibo(n))

# 25501

# def recursion(s, l, r,cnt):
#    if l >= r: return 1, cnt
#    elif s[l] != s[r]: return 0, cnt
#    else: return recursion(s, l+1, r-1,cnt+1)

# def isPalindrome(s):
#    cnt = 1
#    return recursion(s, 0, len(s)-1,cnt)

# import sys
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#    li = input().strip()
#    print(*isPalindrome(li))

# return 1, cnt -> 튜플형식으로 반환됨.

# 24060
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# tmp = [0] * N
# cnt = 0
# ans = -1

# def merge(p, q, r):
#    global cnt, ans
#    i, j, t = p, q + 1, p

#    # 두 구간 병합(tmp에 담기)
#    while i <= q and j <= r:
#        if A[i] <= A[j]:
#            tmp[t] = A[i]
#            i += 1
#        else:
#            tmp[t] = A[j]
#            j += 1
#        t += 1

#    while i <= q:
#        tmp[t] = A[i]
#        i += 1
#        t += 1

#    while j <= r:
#        tmp[t] = A[j]
#        j += 1
#        t += 1

#    # tmp -> A 로 복사 (이 순간이 ‘저장’으로 카운트)
#    for k in range(p, r + 1):
#        A[k] = tmp[k]
#        cnt += 1
#        if cnt == K:
#            ans = A[k]

# def merge_sort(p, r):
#    if p < r:
#        q = (p + r) // 2
#        merge_sort(p, q)
#        merge_sort(q + 1, r)
#        merge(p, q, r)

# merge_sort(0, N - 1)
# print(ans)

# merge sort 이해한다고 한참 걸리고 내부는 크게 안어려움.
# global <- 전역변수 쓰기하려면 선언해야함. 전역변수 읽기만하려면 필요없음.

# 4779
# import sys

# def kanto(s,p,q):
#    if q-p >1:
#        a=p+(q-p)//3
#        b=p+(q-p)//3*2
#
#        kanto(s,p,a)
#        for i in range(a,b):
#            s[i]=' '
#        kanto(s,b,q)

# for line in sys.stdin:
#    n = int(line)

#    s = ['-' for _ in range(3**n)]
#    kanto(s,0,len(s))

#    print(''.join(s))

# 처음에 일단 함수 짜는데도 꽤 걸렸고, 조건문 잡아주는데도 시간 좀 걸림.(len(s)>1 이대로 무한으로 돌았음)
# for line in sys.stdin <- 파일의 끝까지 불러오기
# for i in range(a,b) s[i]= '' => s[a:b] = '' * (b-a) 슬라이싱으로 간결하게

# 2447
import sys

input = sys.stdin.readline

n = int(input())

li = [["*"] * n for _ in range(n)]


def space(a, b, len):
    for l in range(a, a + len):
        for m in range(b, b + len):
            li[l][m] = " "


def recur(x, y, len):
    if len == 1:
        return
    len = len // 3
    a = x + len
    b = y + len

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                space(a, b, len)
            else:
                recur(x + len * i, y + len * j, len)


recur(0, 0, n)

for i in range(n):
    print("".join(li[i]))

# 암산으로 한다고 대갈통 터지는줄. BUT 깔끔 아주 나이스

# 11729

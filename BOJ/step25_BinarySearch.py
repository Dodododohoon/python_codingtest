# 탐색 구간을 절반으로 줄이면서 찾는 알고리즘 O(log N)
# left, right, mid => right = mid -1, left = mid+1
# left > right 까지 반복

# 1920
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# li_n = list(map(int, input().split()))
# m = int(input())
# li_m = list(map(int, input().split()))
#
# li_n.sort()
#
# def search(k,left,right):
#    if left > right:
#        return '0'
#    mid = (left + right)//2
#
#    if k == li_n[mid]:
#        return '1'
#
#    if k < li_n[mid]:
#        return search(k, left, mid-1)
#    else:
#        return search(k, mid+1, right)
#
# for x in li_m:
#    print(search(x,0,len(li_n)-1))

# 10816
# import sys
# input = sys.stdin.readline

# n = int(input())
# li_n = list(map(int, input().split()))
# m= int(input())
# li_m = list(map(int, input().split()))

# dic = dict()

# for x in li_n:
#    if x in dic:
#        dic[x] +=1
#    else:
#        dic[x] = 1

# out = []

# for x in li_m:
#    if x in dic:
#        out.append(dic.get(x))
#    else:
#        out.append(0)

# print(' '.join(map(str, out)))

# -------------밑에 bisect 표준 라이브러리 아이디어로 풀 수 있음 ------------
# from bisect import bisect_left, bisect_right
# arr = [1, 2, 2, 2, 3, 4, 5]
# print(bisect_left(arr, 2))   # 1  ← 2가 처음 나오는 위치
# print(bisect_right(arr, 2))  # 4  ← 2가 끝난 다음 위치
# print(bisect_right(arr, 2) - bisect_left(arr, 2))  # 3개

# 1654
# import sys

# input = sys.stdin.readline

# k, n = map(int, input().split())
# li = [int(input()) for _ in range(k)]


# def search(cnt, left, right):
#     ans = 0
#     while left <= right:
#         mid = (left + right) // 2
#         total = 0
#         for x in li:
#             total += x // mid

#         if total >= cnt:
#             ans = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return ans


# print(search(n, 1, max(li)))

# 다시 풀어보자
# 이분탐색을 할 꺼면 확실하게 이분탐색으로 쭉.

# 2805
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# li = list(map(int, input().split()))

# li.sort(reverse=True)

# def search(left, right,m):
#    h = 0
#    while left <= right:
#        total=0
#        mid = (left + right)//2
#
#        for x in li:
#            if x <= mid:
#                break
#            total += x - mid
#
#        if total == m:
#            h= mid
#            break
#        elif total > m:
#            h=mid
#            left = mid +1
#        else:
#            right = mid -1

#    return h

# print(search(0,li[0],m))


# mid로만 풀릴 줄 알고 mid로 경우 분석하다가 안풀려서 h 쓰니깐 바로 해결됨.
# 뭔 차이인지 확실하게 이해됨.
# mid써서 한번 더 돌리는 건 검증들어가는 거임. 더 있는지.
# 그니깐 검증 들어가기 전 값이 확실한 정답 값이 되는 거. mid값이 답이 아니라.

# 2110
# import sys

# input = sys.stdin.readline

# n, c = map(int, input().split())
# arr = [int(input()) for _ in range(n)]
# arr.sort()

# last = arr[0]


# 1300


# 12015


# ----------------review-----------------
# 1920
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))

# arr.sort()

# for x in check:
#     left = 0
#     right = len(arr) - 1
#     ans = 0
#
#     while left <= right:
#         mid = (left + right) // 2
#

#         if arr[mid] == x:
#             print("1")
#             ans = 1
#             break
#         elif arr[mid] > x:
#             right = mid - 1
#         else:
#             left = mid + 1

#     if ans == 0:
#         print("0")

# 10816     다시 풀어보자 딕셔너리, 이분탐색 둘다. bisect로도
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# m = int(input())
# check = list(map(int, input().split()))

# arr.sort()


# def lower(x):
#     lo, hi = 0, len(arr)

#     while lo < hi:
#         mid = (lo + hi) // 2

#         if arr[mid] >= x:
#             hi = mid
#         else:
#             lo = mid + 1

#     return hi


# def upper(x):
#     lo, hi = 0, len(arr)
#     while lo < hi:
#         mid = (lo + hi) // 2

#         if arr[mid] > x:
#             hi = mid
#         else:
#             lo = mid + 1

#     return hi


# for x in check:

#     low, high = lower(x), upper(x)

#     print(high - low, end=" ")


# dic = dict()      #딕셔너리 버전

# for x in arr:
#     if not x in dic:
#         dic[x] = 1
#     else:
#         dic[x] += 1

# for x in check:
#     if x in dic:
#         print(dic.get(x), end=" ")
#     else:
#         print("0", end=" ")

#1654
#import sys
#input = sys.stdin.readline

#k,n = map(int, input().split())
#arr = [int(input()) for _ in range(k)]
#arr.sort()

#left, right = 0, arr[-1]

#while left <= right:
#    half = (left + right)//2
#    cnt = 0
#    
#    if right == 1:
#        print('1')
#        exit()
#    
#    for x in arr:
#        cnt += x//half
#    
#    if cnt < n:
#        right = half -1
#    else:
#        left = half+1

#print(right)

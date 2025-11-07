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
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
li = [int(input()) for _ in range(k)]


def search(cnt, left, right):
    if left > right:
        return
    total = 0
    mid = (left + right) // 2

    for x in li:
        total += x // mid

    if total == cnt:
        return mid

    if total > cnt:
        return search(cnt, mid + 1, right)
    else:
        return search(cnt, left, mid - 1)


total = n
num = search(n, 0, min(li))

while total == n:
    total = 0
    num += 1
    for x in li:
        total += x // num

print(num - 1)

# 2805


# 2110


# 1300


# 12015

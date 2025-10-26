# 1037
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))

# li.sort()

# print(li[0] * li[-1])

# sort하면 O(nlogn)이라서 그냥 min/max쓰면 O(n)이어서 더 심플

# 25192
# import sys

# input = sys.stdin.readline

# n = int(input())
# enter = set()
# cnt = 0

# for _ in range(n):
#     s = input().strip()

#     if s == "ENTER":
#         enter.clear()
#     elif not s in enter:
#         enter.add(s)
#         cnt += 1

# print(cnt)

# 처음에 list썼다가 시간초과떠서 set으로 변경하고 clear

# 26069


# 2108


# 20920

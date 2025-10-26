# 1037
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))

# li.sort()

# print(li[0] * li[-1])

# sort하면 O(nlogn)이라서 그냥 min/max쓰면 O(n)이어서 더 심플

# 25192
import sys

input = sys.stdin.readline

n = int(input())
li = []
cnt = 0

for _ in range(n):
    s = input().strip()

    if s == "ENTER":
        li.clear()
    elif not s in li:
        li.append(s)
        cnt += 1

print(cnt)
# 26069


# 2108


# 20920

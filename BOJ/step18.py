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
#import sys
#input = sys.stdin.readline

#n = int(input())

#li=['ChongChong']

#for _ in range(n):
#    a, b = map(str, input().split())
#    if a in li and b in li:
#        continue
#    if a in li:
#        li.append(b)
#        continue
#    if b in li:
#        li.append(a)

#print(len(li))

#set쓰면 훨씬 시간 save하면서 풀 수 있네.. in li 이거도 안해줘도 되고.
# 2108


# 20920

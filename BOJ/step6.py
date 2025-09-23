# 25083
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

# 3003
# import sys

# li1 = [1, 1, 2, 2, 2, 8]
# li2 = list(map(int, sys.stdin.readline().split()))

# for i in range(6):
#    print(li1[i] - li2[i], end=" ")

# 2444
# n = int(input())
# for i in range(2 * n - 1):
#     if i <= n - 1:
#         print(" " * ((n - 1) - i), "*" * (2 * i + 1), " ", sep="")
#     else:
#         print(" " * (i - (n - 1)), "*" * (2 * ((2 * n - 2) - i) + 1), " ", sep="")

# 10988
import sys

# li = sys.stdin.readline().strip()
# if li == li[::-1]:
#     print("1")
# else:
#     print("0")

# 1157
import sys

li = sys.stdin.readline().strip()
li_ord = list(map(ord, li.upper()))  # 65'A'~90'Z'
li_cnt = [0] * 26

for i in range(65, 91):
    li_cnt[i - 65] = li_ord.count(i)

if li_cnt.count(max(li_cnt)) == 1:
    idx = li_cnt.index(max(li_cnt))
    print(chr(idx + 65))
else:
    print("?")

# 2941

# 1316

# 25206

#1715
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

sum = arr[0] + arr[1]
for x in arr[2:]:
  total = sum + x
  sum += total

print(sum)
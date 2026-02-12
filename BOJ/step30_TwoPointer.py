# 정렬된 배열에서 두개의 포인터(인덱스)를 양쪽 끝에 두고 조건을 만족시킬 때까지
# 포인터를 움직이며 탐색하는 방식
#    if li < target:
#        i += 1        # 합을 키움
#    elif li > target:
#        j -= 1        # 합을 줄임
#    else:
#        count,  i += 1, j -= 1 #정답 찾음

# 3273
# import sys
# input = sys.stdin.readline

# n = int(input())

# li = list(map(int, input().split()))
# x = int(input())

# li.sort()

# i=0
# j=len(li) -1
# cnt=0

# while i<j:
#    k = li[i] + li[j]
#
#    if k < x:
#        i +=1
#    elif k > x:
#        j -=1
#    else:
#        cnt +=1
#        i +=1
#        j -=1

# print(cnt)

# 2470
# import sys

# input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))

# li.sort()

# i = 0
# j = len(li) - 1
# m = abs(li[0] + li[-1])
# a = i
# b = j

# while i < j:
#     ans = li[i] + li[j]
#     if abs(ans) < m:
#         m = abs(ans)
#         a = i
#         b = j

#     if ans == 0:
#         break
#     elif ans > 0:
#         j -= 1
#     else:
#         i += 1

# print(li[a], li[b])

# 변수명 좀 다듬을 필요 있음.
# 나머지는 클린.


# 1806
# import sys

# input = sys.stdin.readline

# n, s = map(int, input().split())

# li = list(map(int, input().split()))

# pre = [0] * (n + 1)

# for i in range(1, n + 1):
#     pre[i] = pre[i - 1] + li[i - 1]

# start = 0
# end = 1
# min_len = 100000
# while start < end:
#     if min_len==1:
#         break
#     if end > n:
#         break
#     pre_sum = pre[end] - pre[start]
#     if pre_sum >= s:
#         if end - start < min_len:
#             min_len = end - start
#         start += 1
#     else:
#         end += 1


# if min_len == 100000:
#     print("0")
# else:
#     print(min_len)

# prefix_sum 안써도 되네? 그냥 sum += end, -= start 요론식으로 바로 가능. (슬라이딩 윈도우)

# 1644


# 1450


#-----------------------REVIEW---------
#3273
#import sys
#input =sys.stdin.readline

#n = int(input())
#arr = list(map(int,input().split()))
#target = int(input())

#arr.sort()

#cnt = 0
#i=0
#j=len(arr)-1

#while i<j:
#    sum = arr[i] + arr[j]
#    
#    if sum == target:
#        cnt +=1
#        i +=1
#        j -=1
#    elif sum < target:
#        i+=1
#    else:
#        j -= 1
#        
#print(cnt)

#1806
#import sys
#input = sys.stdin.readline

#n, s = map(int, input().split())
#arr = list(map(int, input().split()))

#prefix = [0] * (n+1)

#for i in range(1,n+1):
#    prefix[i] = prefix[i-1] + arr[i-1]
#    
#left, right = 0, 1
#size = 100001

#while right <= n:
#    pre_sum = prefix[right] - prefix[left]
#    
#    if pre_sum >= s:
#        size = min(size,right-left)
#        if size ==1:
#            print('1')
#            exit()
#        left += 1
#    else:
#        right +=1

#if size == 100001:
#    print('0')
#else:
#    print(size)
    
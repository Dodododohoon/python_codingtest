#정렬된 배열에서 두개의 포인터(인덱스)를 양쪽 끝에 두고 조건을 만족시킬 때까지
#포인터를 움직이며 탐색하는 방식
#    if li < target:
#        i += 1        # 합을 키움
#    elif li > target:
#        j -= 1        # 합을 줄임
#    else:
#        count,  i += 1, j -= 1 #정답 찾음

#3273
#import sys
#input = sys.stdin.readline

#n = int(input())

#li = list(map(int, input().split()))
#x = int(input())

#li.sort()

#i=0
#j=len(li) -1
#cnt=0

#while i<j:
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

#print(cnt)

#2470


#1806


#1644


#1450


#10807
#n = int(input())
#data = list(map(int, input().split()))
#check = int(input())
#count = 0
#li=[]

#for i in range (n):
#    li.append(data[i])

#for i in range(n):
#    if li[i]==check:
#        count +=1
#print(count)
#
#n=int(input())
#data = list(map(int, input().split()))
#check = int(input())
#count =0

#for i in range(n):
#    if data[i] ==check:
#        count += 1
#print(count)

#print(data.count(check)) - 슈퍼 심플

#10871
#size, num = map(int, input().split())
#data = list(map(int, input().split()))

#for i in range(size):
#    if(data[i]<num):
#        print(f"{data[i]}", end=" ")
        
#for x in data: 더 심플
#    if(x<num):
#        print(x)

#10818
#size = int(input())
#data = list(map(int, input().split()))

#max=data[0]
#min=data[0]

#for x in data:
#    if x >max:
#        max =x
#    if x < min:
#        min =x
#print(min, max)

#print(min(data), max(data)) -> 심플

#2562
#li=[]
#for i in range(9):                    nums = [int(input()) for _ in range(9)] <- 심플
#    li.append(int(input()))
#max_val = max(li)
#index = li.index(max_val)
#print(max_val)
#print(index+1)

#10810
#n, m = map(int, input().split())
#li = [int(0) for _ in range(n)]

#for a in range(m):
#    i, j, k = map(int, input().split())
    #for idx in range(i-1,j):                #for i in range(j)해둬서 문제 발생. 루프 변수는 시작값으로 계속 재할당 됨.
    #    li[idx]=k
#    li[i-1:j] = [k] * (j - (i - 1))              -> 심플
#for b in range(n):
#    print(li[b], end =" ")        
#print(*li)

#10813
#n, m = map(int, input().split())
#li = [0] * n                            # li = list(range(1,n+1))
#for b in range(n):
#    li[b]=b+1

#for a in range(m):
#    i, j =map(int, input().split())
#    temp = li[i-1]                # li[i-1], li[j-1] = li[j-1], li[i-1]
#    li[i-1]=li[j-1]
#    li[j-1]=temp

#print(*li)

#5597
#li=list(range(1,31))  # li = set(range(1,31))을 쓰면 O(n) ->O(1)로 줄어듬

#for i in range(28):
#    n = int(input())        #li.remove(int(input())) 가능
#    li.remove(n)
#                                       #set 쓸꺼면 여기서 sort한번 해줘야함. set은 뒤죽박죽
#print(li[0])
#print(li[1])

#3052
#s1 = set()
#for i in range(10):
#    s1.add(int(input())%42)
#print(len(s1))
#print(len({int(input()) % 42 for _ in range(10)})) 한줄 풀이도 있네,,, 여윽시 파이썬

#10811                #list[i:j]는 i부터 j-1까지.
#n, m = map(int, input().split())
#li = list(range(1,n+1))

#for _ in range (m):
#    i, j = map(int, input().split())
#    if (i ==1):                                    #li [i-1:j] = li[i-1:j][::-1] <- 이렇게 하면 훠얼씬 수월
#        li[i-1:j] = li[j-1::-1]
#    else:
#        li[i-1:j] = li[j-1:i-2:-1]
#print(*li)

#1546
#import sys
#n = int(sys.stdin.readline())
#score = list(map(int, sys.stdin.readline().split()))
#n_score = [0] * len(score)

#for i in range (len(score)):                   #n_score=[s/max*100 for s in score] 이렇게 한줄로 가능.
#    n_score[i] = score[i]/max(score)*100

#print(sum(n_score)/len(n_score))

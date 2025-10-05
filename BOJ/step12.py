# 2798
# n, m = map(int, input().split())
# li= list(map(int,input().split()))
# s = set()

# for i in range(n):
#    for j in range(i+1,n):
#        for k in range(j+1,n):
#            if li[i] + li[j] + li[k] == m:
#                s.add(li[i] + li[j] + li[k])
#                break
#            if li[i] + li[j] + li[k] <= m:
#                s.add(li[i] + li[j] + li[k])
#        if li[i] + li[j] + li[k] == m:
#            break
#    if li[i] + li[j] + li[k] == m:
#        break
# print(max(s))

# max를 구하는 문제다 보니 굳이 set을 쓸필요가 없었다. + break를 넣는게 조금 이라도 더 횟수를 줄일 수 있을 거라고 생각 했는데 별 차이 안난다고 하네. 게다가 더 실수가 날 수 있다고 하지마래

# 2231
# n = int(input())
# tmp =n
# k = 0
# num=0

# while tmp !=0:
#     tmp//=10
#     k+=1

# for i in range(max(1,n-9*k), n):
#      digit = list(map(int, str(i)))
#      m=i

#      if m + sum(digit) == n:
#          num=m
#          break

# print(num)

# 처음에는 자리수 10 나머지로 하나하나 뽑아주다가 메모리,시간에러 떠서 digit방식 찾아서 바로 list로 뽑아서 풀었는데, valueError 떠서 빡쳐서 gpt 물어보니 n=10같은 경우에 시작점이 음수여서 list(map(int, str(i))) 여기서 에러가 뜸. 그래서 max(1, )해서 최소 시작점을 1로 만듦.

# 19532
#a, b, c, d, e, f = map(int, input().split())
#ans = (e * c - f * b) / (a * e - d * b)


#for x in range(-999, 1000):
#    if x == ans:
#        y = (a * f - c * d) / (a * e - b * d)
#        print(x, int(y))

# y=(c-ax)/b 이걸로 구하니깐 ZeroError 떠서 걍 아에 깔끔하게 바꾸니깐 돌아간다. 귀찮더라도 저게 맞는 듯.

# 1018
#import sys

#n, m = map(int, sys.stdin.readline().split())
#li=[]
#li1=[[0]*m for _ in range(n)]
#li2=[[0]*m for _ in range(n)]

#for _ in range(n):
#    li.append(list(sys.stdin.readline().strip()))

#for i in range(n):
#    for j in range(m):
#            if (i+j) % 2==0:
#                    if li[i][j] == 'B':
#                        li1[i][j]=1
#                    else:
#                        li2[i][j]=1
#            else:
#                    if li[i][j] == 'B':
#                        li2[i][j]=1
#                    else:
#                        li1[i][j]=1
#col=0
#row=0
#num=5000              
#while col + 8 <=n:        
#    sum1=0
#    sum2=0
#    for i in range(col,col+8):
#        sum1 += sum(li1[i][row:row+8])
#        sum2 += sum(li2[i][row:row+8])
#    if (min(sum1,sum2) <num):
#        num = min(sum1,sum2)
#    
#    if row + 8 >= m:
#        row = 0
#        col +=1
#    else:
#        row +=1

#print(num)

#인덱스 틀렸음 [row:row+7] 했었음. 인덱스도 끝부분은 포함 안함
#연산자 잘못 씀. row +8 <=m 했었음..
#보조리스트 안만들어도 되네? 그냥 바로 8칸8칸 조사하는 방식 가능. 근데 4중 for문 이네 ,,, 근데 별차이도 없고 오히려 얘가 더 유리하대 ㅜ

# 1436
#n= int(input())
#cnt=0
#K=666
#num=0

#while(cnt<n):
#    li = list(map(int, str(K)))
#    for i in range(len(li)-2):
#        if li[i] ==6 and li[i+1] ==6 and li[i+2] ==6:
#            cnt +=1
#            num=K
#            break
#    K+=1
#print(num)

#나름 빨리 풀었는데 '666' in str(num) 이렇게 해서 바로 구할 수도 있네,,,

# 2839
n =int(input())
num =2000
k_5=0

while n>0:
    total=0
    k_3=0
          
    if n%5==0:
        num=n//5
        break
        
    if n%3==0:
        k_3+=n//3
        total = k_5 + k_3   
        if(total <num):
            num =total
    n=n-5
    k_5+=1

if(num==2000):
    print('-1')
else:    
    print(num)
        
# 왜 오래 걸렸는지 이해가 안되노, 한번 꼬여버리니깐 툭툭 하나씩 하다가 오히려 더 꼬임.
# 조건문에서 걸리면 
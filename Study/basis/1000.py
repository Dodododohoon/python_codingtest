#a = map(int, input().split())
#print(a)

a, b =map(int, input().split())
print(a+b)

#첫번째 a는 map 형식으로 되어있음. 두번째 a, b는 map에서 int 할당이 된거임.
#map는 임시 처리 객체로 생각하면됨. 큰 입출력이 생겼을 때, 다 list나 tuple로 받아두고 처리하면 데이터가 많이 쓰이니깐. map으로 처리할껀 처리하고 받아오면 데이터 낭비 훨씬 줄음.
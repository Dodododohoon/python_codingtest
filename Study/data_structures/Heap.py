🧠 Python Heap (heapq) 요약 노트
✅ 개념
- **힙(Heap)**: 완전이진트리 기반의 자료구조  
- `heapq`는 **최소 힙(min heap)** 기반  
- 부모 ≤ 자식 → 가장 작은 값이 루트에 위치  
- **최대 힙**은 `음수 변환(-x)`으로 구현  

⚙️ 기본 사용법
```python
import heapq

heap = []

# 추가
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

# 최소값 확인/제거
print(heap[0])         # 1
print(heapq.heappop(heap))  # 1
```

---

## 💥 최대 힙 구현
```python
heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -8)
print(-heapq.heappop(heap))  # 8
```

---

## 🔁 리스트 → 힙 변환
```python
li = [4, 1, 7, 3, 8, 5]
heapq.heapify(li)
print(li)  # [1, 3, 5, 4, 8, 7]
```

---

## 🧩 우선순위 큐
```python
tasks = []
heapq.heappush(tasks, (2, 'coding'))
heapq.heappush(tasks, (1, 'eat'))

while tasks:
    p, t = heapq.heappop(tasks)
    print(p, t)

# 출력: 1 eat / 2 coding
```

---

## 🧮 유용한 함수
| 함수 | 설명 |
|------|------|
| `heappush(heap, x)` | 원소 추가 |
| `heappop(heap)` | 최소값 제거 |
| `heapify(list)` | 리스트를 힙으로 변환 |
| `nsmallest(k, it)` | 가장 작은 k개 |
| `nlargest(k, it)` | 가장 큰 k개 |

---

## 💯 백준 예시

### 🧩 1927 — 최소 힙
```python
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, x)
```

### 🔥 11279 — 최대 힙
```python
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -x)
```

---

✅ **정리 요약**
| 구분 | 최소 힙 | 최대 힙 |
|------|----------|----------|
| 삽입 | `heappush(h, x)` | `heappush(h, -x)` |
| 삭제 | `heappop(h)` | `-heappop(h)` |
| 확인 | `h[0]` | `-h[0]` |
# 14. 연결 리스트 (Linked List)

## 구현 내용

단순 연결 리스트(Singly Linked List)를 직접 구현. 노드는 값(data)과 다음 노드를 가리키는 포인터(next)를 가진다.

- `Node` 클래스: 한 칸 = 데이터 + 다음 화살표
- `LinkedList.append(data)`: 리스트 끝에 노드 추가
- `LinkedList.print_list()`: 모든 값을 앞에서부터 순회하며 반환

## 공부하면서 이해한 것

### 1. Node를 만들 때 next를 None으로 초기화하는 이유

```python
def __init__(self, data):
    self.data = data
    self.next = None  # 아직 다른 노드가 만들어지지 않았으니까 None으로 초기화
```

새로 만든 노드는 아직 어디에도 연결되어 있지 않은 상태다. "다음이 없다(None)"로 두고, 나중에 append에서 누군가의 next에 꽂아주는 순간 연결이 생긴다. 반대로 마지막 노드는 항상 next가 None이므로, "next가 None인 노드 = 마지막 노드"라는 판별 기준으로도 쓰인다.

### 2. head의 역할과 이동용 변수 cur이 필요한 이유

각각의 노드를 개별적으로 만들고, 그 노드들을 연결해서 리스트를 구성한다. head는 리스트의 시작점(첫 번째 노드)을 가리키는 포인터 역할.

```python
cur = self.head  # 이동식 cur을 설정해줘야 됨
while cur.next is not None:
    cur = cur.next
cur.next = new_node
```

cur 없이 `self.head = self.head.next`처럼 head를 직접 움직이면 리스트의 시작점 자체가 바뀌어서 앞 노드들을 영영 잃어버린다. head는 손잡이라서 고정해두고, 이동은 복사본(cur)으로 한다. `cur = cur.next`는 화살표를 한 칸 따라가는 동작이다.

### 3. append의 두 가지 경우

- 리스트가 비어 있으면 (`self.head is None`): head에 새 노드를 바로 꽂고 return
- 노드가 있으면: head부터 시작해 `cur.next`가 None인 마지막 노드까지 이동한 뒤 `cur.next = new_node`

두 경우를 나누는 이유: 빈 리스트는 따라갈 화살표 자체가 없어서 `cur.next`에 접근하는 순간 에러가 나기 때문이다.

### 4. 순회 종료 조건의 차이 (append vs print_list)

- append: `while cur.next is not None` -> 마지막 노드"에서" 멈춰야 함 (거기에 새 노드를 붙여야 하니까)
- print_list: `while cur is not None` -> 마지막 노드"까지 지나가야" 함 (모든 값을 읽어야 하니까)

한 글자 차이(`cur` vs `cur.next`)로 멈추는 위치가 달라진다.

### 5. 배열(파이썬 list)과의 비교

| 구분 | 배열 | 연결 리스트 |
|---|---|---|
| 메모리 | 연속된 칸 | 떨어진 칸 + 화살표 |
| 인덱스 접근 | O(1) | O(N) (앞에서부터 따라가야 함) |
| 맨 앞 삽입/삭제 | O(N) (뒤를 다 밀어야 함) | O(1) (head만 바꾸면 됨) |
| 끝에 추가 | O(1) | O(N) (tail 포인터가 없는 현재 구현 기준) |

삽입/삭제가 잦은 곳(스택, 큐, 그래프 등)에서 연결 리스트가 유리하다.

## 실행 결과

```
=== 연결 리스트 테스트 ===
1
2
3
리스트: [1, 2, 3]

=== 연결 리스트 테스트 2 ===
10
20
30
40
리스트: [10, 20, 30, 40]
```

`ll.append(1)` -> `ll.append(2)` -> `ll.append(3)` 실행 시 내부 상태 변화:

```
초기:        head -> None
append(1):   head -> [1|None]                       (빈 리스트라 head에 바로 꽂음)
append(2):   head -> [1|.] -> [2|None]              (cur이 1에서 멈춤, 1.next = 새 노드)
append(3):   head -> [1|.] -> [2|.] -> [3|None]     (cur이 1 -> 2로 이동 후 2.next = 새 노드)
```

print_list()의 cur 이동 순서: 1 출력 -> 2 출력 -> 3 출력 -> cur이 None이 되어 종료 -> [1, 2, 3] 반환

## 더 알아볼 것

- [ ] tail 포인터를 추가해서 append를 O(1)로 만들기
- [ ] 중간 삽입(insert), 삭제(delete) 구현
- [ ] 이중 연결 리스트(Doubly Linked List)와의 차이

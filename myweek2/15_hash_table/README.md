# 15. 해시 테이블 - 학생 성적 관리

## 구현 내용

딕셔너리(해시 테이블)로 학생 성적 관리: 평균 계산, 최고점 학생 찾기, 특정 학생 조회

- `manage_grades(students)`: 평균, 최고점 학생 이름, 최고점 반환
- `find_student_score(students, name)`: 특정 학생 점수 조회 (없으면 None)

## 개념: 해시 테이블이 왜 O(1)인가

- 해시 테이블은 Key를 해시 함수에 넣어 나온 해시 값으로 저장 위치를 바로 계산하는 자료구조
- 배열처럼 처음부터 훑을 필요 없이 "Key -> 위치"가 한 번에 나오므로 검색/삽입/삭제가 평균 O(1)
- 파이썬의 dict가 내부적으로 해시 테이블로 구현되어 있음 -> 이번 과제에서 dict를 쓴 이유
- 단, O(1)은 평균이고 충돌이 몰리면 최악 O(N)까지 갈 수 있음
- 충돌 해결 방법
  - 체이닝(Chaining): 같은 해시 값의 Key-Value 쌍을 연결 리스트로 매달기
  - 오픈 어드레싱(Open Addressing): 다른 빈 슬롯 찾기 (선형 탐사, 이차 탐사, 이중 해싱)
- 실무 활용: DB 인덱싱, 캐싱, 집합 연산 등

## 내 코드에서 쓴 것들

### 1. 빈 딕셔너리 방어

```python
aver = sum(students.values()) / len(students) if students else 0
```

students가 비어 있으면 len이 0이라 ZeroDivisionError가 나므로 조건부 표현식으로 방지. 빈 dict는 falsy라서 `if students`만으로 체크 가능하다.

### 2. 최고점 학생 찾기 - max의 key 파라미터

```python
top_s = max(students, key=students.get)
```

- dict를 max에 넘기면 기본적으로 Key(이름)들을 순회함
- `key=students.get`을 주면 각 이름을 `students.get(이름)`에 넣은 결과(=점수)를 비교 기준으로 사용
- 즉 점수로 비교하되, 반환되는 건 이름
- 동점이면 먼저 나온 학생이 반환됨

### 3. 없는 Key 조회 - get vs 대괄호

```python
students.get(name, None)   # 없으면 None 반환
students[name]             # 없으면 KeyError 발생
```

10번 이분 탐색에서 list.index()가 값이 없으면 에러 나던 것과 같은 패턴. "없을 수도 있는 값 조회"는 에러를 내느냐 / 기본값을 주느냐를 선택해야 하는데, 조회 실패가 정상 흐름인 이 문제에서는 get이 적합하다. get의 기본값이 원래 None이라 `students.get(name)`만 써도 동일하다.

## 실행 결과

```
=== 학생 성적 관리 ===
평균 점수: 87.5
최고 점수: David (95점)

=== 학생 점수 조회 ===
Alice의 점수: 85

Eve의 점수: None
```

- manage_grades: (85 + 92 + 78 + 95) / 4 = 87.5, max가 점수 기준으로 비교해 David(95) 반환
- find_student_score("Alice"): dict에 있으므로 85
- find_student_score("Eve"): dict에 없지만 get 덕분에 에러 없이 None

## 알게 된 점 / 주의할 점

- max/min의 key 파라미터는 "무엇으로 비교할지"를 함수로 넘기는 것 (sorted의 key와 같은 개념)
- dict의 Key는 해시 가능(hashable)해야 함 -> 문자열, 숫자, 튜플은 되지만 리스트는 Key로 못 씀
- 발견한 버그: `top_score = students[top_s]`는 students가 빈 dict일 때 top_s가 None이라 KeyError가 남. 바로 윗줄에서 `if students else None`으로 방어했는데 아랫줄의 대괄호 조회가 방어를 무효화함. get을 정확히 쓴 find_student_score와 대비되는, "get vs 대괄호" 차이를 실감한 사례

## 더 알아볼 것

- [ ] 체이닝 방식 해시 테이블을 dict 없이 직접 구현해보기
- [ ] 리스트가 dict의 Key가 될 수 없는 이유 (mutable과 hash의 관계)
- [ ] collections.Counter, defaultdict

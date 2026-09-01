"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 해시 테이블로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)

힌트:
- 딕셔너리 사용
- 평균: sum(scores.values()) / len(scores)
- 최고점: max(scores, key=scores.get)
"""

'''해시 테이블 특징
- Key-Value 쌍으로 데이터를 저장
- 평균 O(1) 시간 복잡도로 검색, 삽입, 삭제 가능
- Key는 고유해야 하며, Value는 중복 가능
- 파이썬의 dict는 내부적으로 해시 테이블로 구현되어 있음

해시 테이블 정의
- 해시 테이블은 데이터를 Key-Value 쌍으로 저장하는 자료구조입니다.
- Key를 해시 함수에 넣어 해시 값을 계산하고, 해당 위치에 Value를 저장합니다.
- 충돌이 발생하면 체이닝이나 오픈 어드레싱 등의 방법으로 해결합니다.
- 파이썬의 dict는 이러한 해시 테이블을 내부적으로 구현하여 제공하며, 평균적으로 O(1) 시간 복잡도로 검색, �삽입, 삭제가 가능합니다.

: 해시 테이블 종류
- 체이닝(Chaining): 충돌이 발생하면 연결 리스트를 사용하여 같은 해시 값을 가진 Key-Value 쌍을 저장합니다.
- 오픈 어드레싱(Open Addressing): 충돌이 발생하면 다른 빈 슬롯을 찾아 Key-Value 쌍을 저장합니다. 대표적인 방법으로 선형 탐사(Linear Probing), 이차 탐사(Quadratic Probing), 이중 해싱(Double Hashing) 등이 있습니다.
: 해시 함수
- 해시 함수는 Key를 입력받아 고정된 크기의 해시 값을 출력하는 함수입니다.
- 좋은 해시 함수는 충돌을 최소화하고, Key의 분포를 균등하게 만들어야 합니다.
- 파이썬의 dict는 내부적으로 해시 함수를 사용하여 Key를 해시 값으로 변환하고, 이를 기반으로 Value를 저장합니다.

- 해시 뜻 
- 해시(Hash)는 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 과정을 의미합니다.
- 해시 테이블(Hash Table)은 이러한 해시 함수를 이용하여 데이터를 저장하고 검색하는 자료구조입니다.
- 해시 테이블은 Key-Value 쌍으로 데이터를 저장하며, Key를 해시 함수에 넣어 해시 값을 계산하고, 해당 위치에 Value를 저장합니다.
- 충돌이 발생하면 체이닝이나 오픈 어드레싱 등의 방법으로 해결합니다.
- 파이썬의 dict는 이러한 해시 테이블을 내부적으로 구현하여 제공하며, 평균적으로 O(1) 시간 복잡도로 검색, 삽입, 삭제가 가능합니다.   

- 실무에서
- 해시 테이블은 데이터베이스 인덱싱, 캐싱, 집합 연산 등 다양한 분야에서 활용됩니다.
- 예를 들어, 데이터베이스에서 특정 레코드를 빠르게 검색하기 위해 해시 테이블을 사용하여 인덱스를 생성할 수 있습니다.
- 또한, 캐시 시스템에서 최근에 사용된 데이터를 빠르게 조회하기 위해 해시 테이블을 활용할 수 있습니다.
- 집합 연산에서는 해시 테이블을 사용하여 두 집합의 교집합, 합집합, 차집합 등을 효율적으로 계산할 수 있습니다.
-
- 해시 테이블은 메모리 사용량이 많을 수 있으므로, 필요한 경우에만 사용하고, 적절한 크기의 해시 테이블을 유지하는 것이 중요합니다.
- 또한, 해시 테이블의 성능은 해시 함수의 품질과 충돌 해결 방법에 따라 달라질 수 있으므로, 상황에 맞는 해시 함수와 충돌 해결 방법을 선택하는 것이 중요합니다.
- 파이썬의 dict는 내부적으로 최적화되어 있어 대부분의 경우에 효율적으로 동작하지만, 특정 상황에서는 성능 저하가 발생할 수 있으므로, 성능 분석과 최적화가 필요할 수 있습니다.


'''
def manage_grades(students):
    """
    학생 성적 관리 시스템
    
    Args:
        students: {이름: 점수} 딕셔너리
    
    Returns:
        평균, 최고점 학생 이름, 최고점
    """
    # TODO: 평균 점수 계산
    aver = sum(students.values()) / len(students) if students else 0 ## 분모에 0이 들어가는 경우를 방지하기 위해 조건문 추가
    
    
    # TODO: 최고 점수 학생 찾기
    top_s = max(students,key=students.get) if students else None 
    top_score= students[top_s] 
    return aver, top_s, top_score

def find_student_score(students, name):
    """
    특정 학생의 점수 조회
    
    Args:
        students: 학생 딕셔너리
        name: 찾을 학생 이름
    
    Returns:
        점수 (없으면 None)
    """
    return students.get(name,None) ## get 함수는 key가 존재하지 않으면 None을 반환하도록 설정

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    
    print("=== 학생 성적 관리 ===")
    avg, top_name, top_score = manage_grades(students1)
    print(f"평균 점수: {avg}")
    print(f"최고 점수: {top_name} ({top_score}점)")
    print()
    
    # 테스트 케이스 2: 학생 조회
    print("=== 학생 점수 조회 ===")
    search_name = "Alice"
    score = find_student_score(students1, search_name)
    print(f"{search_name}의 점수: {score}")
    print()
    
    search_name2 = "Eve"
    score2 = find_student_score(students1, search_name2)
    print(f"{search_name2}의 점수: {score2}")



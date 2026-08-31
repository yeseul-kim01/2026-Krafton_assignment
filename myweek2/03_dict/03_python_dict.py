from collections import defaultdict #딕셔너리 

"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""

## 리스트 안의 구성은 딕셔너리 , 람다로 리스트 안의 딕셔너리의 전체 값의 합을 구한 다음에 평균을 계산하면 됨

def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수
    
    Args:
        students: 학생 정보 딕셔너리 리스트
    
    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """
    #print(students)
    
    ## 한명의 점수 출력하기
    # print(students[0]['score'])# 딕셔너리는 키값이 인덱스가 아님. key값을 이용해서 점수를 출력해야됨.
    all_scores = sum(s['score'] for s in students) # 여기까지의 시간복잡도는 O(n)임. n은 학생 수
    # print(all_scores)
    #평균값
    average = all_scores / len(students)
    # 평균 이상인 학생들만 추출하기 - 리스트의 컴프리헨션을 이용해서 평균 이상인 학생들의 이름만 추출
    above_average_students = [s['name'] for s in students if s['score'] >= average]
    
    # 소숫점 몇자리 까지인지에 대한 정보가 없으니 우선 소숫점 2자리까지 출력하도록 함
    # return round(average, 2), above_average_students
    return average, above_average_students

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")



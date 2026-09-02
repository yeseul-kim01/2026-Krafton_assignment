"""
[큐 - 프린터 대기열]

문제 설명:
- 큐(Queue)를 사용하여 프린터 작업을 순서대로 처리합니다.
- FIFO (First In First Out) 구조를 활용합니다.

입력:
- jobs: 인쇄 작업 리스트 (예: ["문서A", "문서B", "문서C"])

출력:
- 작업이 처리되는 순서

예제:
입력: ["문서A", "문서B", "문서C"]
출력:
처리: 문서A
처리: 문서B
처리: 문서C

힌트:
- 파이썬에서는 리스트로 큐 구현 가능
- append(): 뒤에 추가 (enqueue)
- pop(0): 앞에서 제거 (dequeue)
"""

from collections import deque ## 많이 자주 쓰는 거 - 보통 실무에서 작업 요청? 같은 거 저장할 때 쓰는 거 같음. 앞에서 봤던 stack 이랑은 다르게, queue는 FIFO 구조라서 먼저 들어온 게 먼저 나감. 그래서 프린터 작업 같은 거 처리할 때 쓰임. 
## list 말고 이런 구조를 쓰는 이유는 list의 pop(0) 연산은 O(n) 시간 복잡도를 가지므로 성능이 떨림. 반면, deque의 popleft() 연산은 O(1) 시간 복잡도를 가짐.

def process_print_queue(jobs):
    """
    프린터 작업을 순서대로 처리
    
    Args:
        jobs: 작업 리스트
    
    Returns:
        처리된 작업 리스트
    """
    # TODO: deque로 큐 생성
    queue = deque(jobs)
    print(jobs)
    processed = []
    while queue:
        j = queue.popleft() # 가장 끝에있는 작업을 꺼내면 됨. 먼저 들어갔던거 꺼낸다 생각하면 됨. list 랑 동일! 
        print(f"처리: {j}") ## 출력할 때 쓰는 f 함수 -> f"처리: {j}" 이렇게 하면 j에 들어있는 값이 출력됨. format 용도! 
        processed.append(j)
        ## pop 이니까 따로 지우지 않아도 됨. 
    
    
    # TODO: 큐가 비어있지 않은 동안 반복
    ## 큐에서 작업 꺼내기
    ## 작업 처리 (출력 및 리스트에 추가)
    
    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    jobs1 = ["문서A", "문서B", "문서C"]
    print("=== 프린터 작업 처리 ===")
    result1 = process_print_queue(jobs1)
    print(f"처리 완료: {result1}")
    print()
    
    # 테스트 케이스 2
    jobs2 = ["이메일", "보고서", "사진", "계약서"]
    print("=== 프린터 작업 처리 ===")
    result2 = process_print_queue(jobs2)
    print(f"처리 완료: {result2}")



"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

## stack 은 자료적으로도 중요함.
## 실무에서 자료 저장할 때 각 상황에 맞는 자료구조를 선택하는 것이 중요함.
## 보통 queue, stack, linked list, tree, graph 등등을 상황에 맞게 선택함.
## queue 는 FIFO, stack 은 LIFO 구조를 가지고 있음. 
## 예를 들어 queue 는 실무에서 보통 요청 처리에 사용되고, stack 은 함수 호출이나 표현식 평가 등에 사용됨. 왜냐면 stack 은 LIFO 구조이기 때문에 최근에 들어온 요청을 먼저 처리해야 하는 상황에서 유용함. queue 는 FIFO 구조이기 때문에 요청이 들어온 순서대로 처리해야 하는 상황에서 유용함.

## 사실 지금 예제로 주어진 문제는 stack 을 사용하지 않고도 해결할 수 있음. 왜냐면 괄호 짝 맞추기는 단순히 여는 괄호와 닫는 괄호의 개수를 세어서 비교하면 되기 때문임. 하지만 stack 을 사용하면 더 직관적으로 문제를 해결할 수 있음. 
## 숫자를 기준으로 해서 +1 -1 0 으로 풀면 더 빠르게 풀기도 함.
## 구현적인 측면에서의 풀이 한개랑 스택 풀이 한개가 나올 수 있을 듯. 





## stack 풀이 
# 해당 문제가 stack 과 어울리는 이유는 last in first out 구조 이기 때문임. 괄호는 사실 ( 게 들어가면 한개씩 쌓이고 ) 게 있으면 가장 최근에 들어갔던 ( 를 제외하면 되는 문제임. 만약에 전체 string 을 순회했는데 개수가 안 맞으면 제대로된 괄호가 아닌 거고, ) 게 들어와서 stack 에서 빼려하는데
# 비어있다면 그것 또한 괄호가 제대로 안 맞는 거라 판단하면 됨. 
def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    stack = [] ## stack 은 list 로 구현도 가능하지만 deque로도 가능하다. 하지만 주어진 문제는 list 니까 list 로 ! list 로 구현하면 append, pop 이 가능함. deque 로 구현하면 append, pop, popleft 등등이 가능함.
    
    # TODO: 문자열의 각 문자를 순회
    for i in s: ## 순회시 인덱스가 크게 중요하지 않기 때문에 변수 낭비 없이 s 자체로 순회할거임. 
        if i == '(': ## 여는 괄호 '('면 스택에 추가
            stack.append(i)
        elif i == ')': ## 닫는 괄호 ')'면
            if not stack: ## 스택이 비어있으면 False 반환
                return False
            stack.pop() ## 아니면 스택에서 pop list 에서 pop 은 마지막에 들어온 값을 제거한다.
                        ## python 과 c 의 차이점은 python 은 할당될 때 list 의 크기가 자동으로 늘어나지만 c 는 malloc 으로 메모리를 할당해야 한다. pop을 할 때 python 은 자동으로 메모리를 줄여주지만 c 는 free 를 해줘야 한다.
        else: ## 괄호가 아닌 다른 문자가 들어오면 무시하고 넘어감. 
            continue ## 이건 그냥 항상 해주는게 좋음. 조건에 없어도 ! 
        
    ## 순회가 끝났는데 만약에 stack 이 비어있지 않으면 ( 가 남아있는 거기 때문에 완벽한 괄호 구조가 아님.
    if stack: ## 반복이 끝나면 스택이 비어있는지 확인
        return False
    return True ## stack 이 비어있으면 True 반환



## 단순 구현 풀이 -stack 보다 단순 구현 풀이의 장점 : 메모리 사용량
def is_valid_parentheses_simple(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")



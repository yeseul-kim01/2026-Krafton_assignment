"""
[분할 정복 - 배열의 최댓값 찾기]

문제 설명:
- 분할 정복(Divide and Conquer) 방식으로 배열의 최댓값을 찾습니다.
- 배열을 반으로 나누고, 각 부분의 최댓값을 구한 후 비교합니다.

입력:
- arr: 정수 배열
- left: 시작 인덱스
- right: 끝 인덱스

출력:
- 배열의 최댓값

예제:
입력: [3, 5, 1, 8, 2, 9, 4]
출력: 9

힌트:
- Base case: left == right일 때 arr[left] 반환
- 배열을 반으로 나누어 재귀 호출
- 왼쪽과 오른쪽의 최댓값 중 큰 값 반환
"""

## 여기서 분할 정복을 쓰는 이유는 배열의 크기를 줄여가며 최댓값을 찾기 위해 또 다른 풀이는 반복문을 통해 순회하면서 찾는 방법도 있는데, 분할 정복을 쓰면 병렬 처리가 가능해짐. 시간 복잡도 측면을 배우는 문제는 아니고 로직을 이해하는 문제임.
## 분할정복은 보통 재귀적으로 문제를 해결하는 방식으로, 큰 문제를 작은 문제로 나누어 해결하고, 그 결과를 합쳐서 최종 결과를 얻는 방법. 이 경우, 배열을 반으로 나누어 각 부분의 최댓값을 찾고, 그 두 값을 비교하여 최종 최댓값을 구함. 
## 최댓값을 저장하는 변수를 따로 두지 않고, 재귀적으로 최댓값을 반환받아 비교하는 방식으로 구현할 수 있음.

def find_max_divide_conquer(arr, left, right):
      # 첫번째 호출 - 3, 5, 1, 8 , 2 , 9 , 4 로 들어갔을 때 
    """
    분할 정복으로 최댓값 찾기
    
    Args:
        arr: 배열
        left: 시작 인덱스
        right: 끝 인덱스
    
    Returns:
        최댓값
    """
    # TODO: base case - 원소가 하나면 그 값 반환
    if left == right: # 1. 안 들어감 # 4. 안들어감. left 가 0, right 가 3 이기 때문에 
        return arr[left] ## 볼 원소가 하나라면 그 값이 최댓값으로 바로 반환됨.
    
    # TODO: 중간 지점 계산
    ## 분할 정복의 정의는 배열을 반으로 나누어야 하므로 중간 지점을 계산 해야 함. -> 반으로 나누기 때문에 시간 복잡도가 다른 탐색들보다 낮음.
    mid = (left + right) //2 # 2. mid = 3 으로 들어감. 3번째 인덱스 값이 8임. # 5. mid = 1 으로 들어감. 1번째 인덱스 값이 5임.

    
    # TODO: 왼쪽 절반의 최댓값
    ## 분할 정복은 각 분할된 부분들을 재귀적으로 호출해서 찾는 용도임. 


    find_max_left= find_max_divide_conquer(arr, left, mid) ## 왼쪽 절반의 최댓값을 재귀적으로 호출하여 찾음.왼쪽 부분이니까 right 의 인덱스 값이 mid 로 들어감. 이 친구가 계속적으로 호출되면서 최종적으로 최댓값을 반환하게 됨. 
    ## 3. find_max_left= find_max_divide_conquer(arr, 0, 3) -> 3번째 인덱스 값이 8임. # 6. find_max_left= find_max_divide_conquer(arr, 0, 1) -> 1번째 인덱스 값이 5임. 
    
    find_max_right= find_max_divide_conquer(arr, mid+1, right) ## 오른쪽 절반의 최댓값을 재귀적으로 호출하여 찾음. 오른쪽 부분이니까 left 의 인덱스 값이 mid+1 로 들어감. 이 친구가 계속적으로 호출되면서 최종적으로 최댓값을 반환하게 됨.
    
    # TODO: 둘 중 큰 값 반환
    return max(find_max_left, find_max_right)
    ## 이부분을 테케로 각 재귀호출에 들어갔을 때 어떻게 나오는지 확인해보자면 
    
    ## 3, 5, 1, 8 , 2 , 9 , 4 로 들어갔을 때 
    
    '''
    
        find_max_divide_conquer(arr, 0, 6)
        │
        ├─ mid = 3
        │
        ├─ find_max_divide_conquer(arr, 0, 3)
        │  │
        │  ├─ mid = 1
        │  │
        │  ├─ find_max_divide_conquer(arr, 0, 1)
        │  │  │
        │  │  ├─ mid = 0
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 0, 0)
        │  │  │      -> return 3
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 1, 1)
        │  │  │      -> return 5
        │  │  │
        │  │  └─ return max(3, 5) = 5
        │  │
        │  ├─ find_max_divide_conquer(arr, 2, 3)
        │  │  │
        │  │  ├─ mid = 2
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 2, 2)
        │  │  │      -> return 1
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 3, 3)
        │  │  │      -> return 8
        │  │  │
        │  │  └─ return max(1, 8) = 8
        │  │
        │  └─ return max(5, 8) = 8
        │
        ├─ find_max_divide_conquer(arr, 4, 6)
        │  │
        │  ├─ mid = 5
        │  │
        │  ├─ find_max_divide_conquer(arr, 4, 5)
        │  │  │
        │  │  ├─ mid = 4
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 4, 4)
        │  │  │      -> return 2
        │  │  │
        │  │  ├─ find_max_divide_conquer(arr, 5, 5)
        │  │  │      -> return 9
        │  │  │
        │  │  └─ return max(2, 9) = 9
        │  │
        │  ├─ find_max_divide_conquer(arr, 6, 6)
        │  │      -> return 4
        │  │
        │  └─ return max(9, 4) = 9
        │
        └─ return max(8, 9) = 9
    
    
    [3, 5, 1, 8, 2, 9, 4]

          f(0,6)
         /     \
      f(0,3)   f(4,6)
      /   \     /   \
   f(0,1) f(2,3) f(4,5) f(6,6)
   /  \    / \     / \      |
 f(0,0)f(1,1) f(2,2)f(3,3) f(4,4)f(5,5)
   3      5      1     8      2     9
      \    /       \   /       \   /
        5            8           9
          \           |           /
             \         8          /
               \________________/
                       9
                       
                       
    위에까지가 분할 정복이고 원래 해당 문제는 순회문으로도 풀 수 있는데 
    [3, 5, 1, 8, 2, 9, 4]
    ↓  ↓  ↓  ↓  ↓  ↓  ↓
    3 -> 5 -> 5 -> 8 -> 8 -> 9 -> 9
                ↑
            현재까지의 최댓값
    
    이게 순회문임. 현개까지의 최댓값을 계속 갱신하면서 최종적으로 최댓값을 찾는 방식임.
    
    시간복잡도 측면에서 보면 큰 차이는 없음! 재귀 구조를 이해하기 좋음. 
    
    
    기본 탐색:
        전체를 한 번 순회해서 최댓값을 갱신
        -> O(n), 단순, 직관적

    분할 정복:
        배열을 반으로 나누고 재귀적으로 최댓값을 구한 뒤 비교
        -> O(n), 구조적, 재귀 설계 학습용
    '''
    
    
    

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    result1 = find_max_divide_conquer(arr1, 0, len(arr1) - 1)
    print(f"배열: {arr1}")
    print(f"최댓값: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [10, 20, 30, 40, 50]
    result2 = find_max_divide_conquer(arr2, 0, len(arr2) - 1)
    print(f"배열: {arr2}")
    print(f"최댓값: {result2}")
    print()
    
    # 테스트 케이스 3
    arr3 = [100]
    result3 = find_max_divide_conquer(arr3, 0, len(arr3) - 1)
    print(f"배열: {arr3}")
    print(f"최댓값: {result3}")



"""
[이분 탐색 - Binary Search]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색 알고리즘을 구현합니다.
- 배열을 반으로 나누어 탐색 범위를 절반씩 줄여갑니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
출력: 3

힌트:
- left, right 포인터 사용
- mid = (left + right) // 2
- arr[mid]와 target 비교하여 범위 조정
"""

def binary_search(arr, target):
    """
    이분 탐색 구현
    
    Args:
        arr: 정렬된 배열
        target: 찾을 값
    
    Returns:
        target의 인덱스 (없으면 -1)
    """
    left = 0
    right = len(arr) - 1
    
    # TODO: left가 right보다 작거나 같을 때까지 반복
    ## 중간 인덱스 계산
    ## arr[mid]와 target 비교
    ## 같으면 mid 반환
    ## target이 더 크면 left = mid + 1
    ## target이 더 작으면 right = mid - 1
    while left <= right: ## left가 right 보다 작거나 같을 때 까지 반복이니까 while 사용.for 은 인덱스를 늘려가는거라 굳이? 횟수 제한 없이 while.
        mid = (left+right) //2 # 중간값 - 하나씩 늘려도 되는 이유 - 정렬되어 있기 때문에 
        if ( arr[mid] == target): # 서로 같으면 해당 값을 찾은거나 마찬가지임. 
            return mid
        elif (arr[mid] < target): # 중간값이 찾고자 하는 값
            left = mid + 1 # 중간값보다 찾고자 하는 값이 크면 왼쪽은 필요없음. mid+1로 바꿔서 오른쪽만 탐색
        else: # 중간값이 찾고자 하는 값보다 크면 오른쪽은
            right = mid - 1 # 오른쪽은 필요없음. mid-1로 바꿔서 왼쪽만 탐색
    
    return -1 # 찾고자 하는 값이 없으면 -1 반환

## 이분 탐색 외의 방법 - 선형 탐색, python 의 in 연산자, index 의 매서드 ,find 매서드 가 있다.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
# 해당 선형 풀이는 시간복잡도가 비효율적임.-> 비효율적일 때가 있음. 이분 탐색은 정렬되어 있는 배열에서만 가능. 정렬되어 있지 않으면 선형 탐색을 사용해야함.

def linear_search_in(arr, target):
    if target in arr:
        return arr.index(target)
    return -1
## index 매서드는 같은 원소가 여러개 있을 때 첫번째 인덱스만 반환함. 하지만 만약 값이 없으면 에러가 발생함. 그래서 in 연산자를 사용하거나 error 핸들링을 해주거나 except 를 사용해줘야 한다.

## index 매서드와 find 매서드의 차이점 - index 는 리스트에서만 사용 가능하지만 find 는 문자열에서도 사용 가능하다. find 는 값이 없으면 -1 반환, index 는 error 발생. 
def linear_search_find(arr, target):
    return arr.find(target) 
## 위에 있는 index 와 find 의 시간 복잡도는 선형 탐색과 똑같음! 왜 똑같냐면 index 와 find 는 내부적으로 선형 탐색을 사용하기 때문임.

    
    

    
# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()
    
    # 테스트 케이스 3: 없는 값
    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")

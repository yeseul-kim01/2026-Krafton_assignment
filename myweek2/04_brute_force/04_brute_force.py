from collections import defaultdict
"""
[완전 탐색 - 배열에서 두 수의 합 찾기]

문제 설명:
- 정수 배열과 목표 값이 주어졌을 때, 배열에서 두 수를 선택하여 
  그 합이 목표 값과 같아지는 모든 쌍을 찾습니다.
- 완전 탐색(Brute Force) 방식으로 모든 경우를 확인합니다.

입력:
- nums: 정수 배열
- target: 목표 합

출력:
- 합이 target이 되는 (i, j) 인덱스 쌍의 리스트 (i < j)

예제:
입력: nums = [2, 7, 11, 15, 3], target = 9
출력: [(0, 1), (0, 4)]
설명: nums[0] + nums[1] = 2 + 7 = 9
      nums[0] + nums[4] = 2 + 7 = 9 (중복이지만 인덱스가 다름)

실제로는: nums[0] + nums[1] = 2 + 7 = 9만 해당

힌트:
- 이중 반복문을 사용하여 모든 쌍을 확인하세요
- i < j 조건을 유지하여 중복을 방지하세요
"""

## 인덱스 출력이 아니면 나열해서 풀수 있는 문제 - 완전 탐색 말고 
## 인덱스 출력이라는 제한이 걸려있기 때문에 굳이 변환할 필요 없이 완전탐색으로 푸는 것이 더 효율적일 거 같음. 
## 아니면 dict 으로 해당 원소 값과 인덱스를 한 쌍으로 묶고, 원소 값으로 오름차순 정렬 후 투 포인터로 값을 구하면 완전 탐색으로 풀지 않아도 됨. 
## 정석적인 풀이는 완전 탐색으로 푸는 것이 맞음.


def find_two_sum_pairs(nums, target):
    """
    배열에서 합이 target이 되는 모든 인덱스 쌍 찾기
    
    Args:
        nums: 정수 배열
        target: 목표 합
    
    Returns:
        list: (i, j) 인덱스 쌍의 리스트
    """
    pairs = []
    n = len(nums)
    
    # # TODO: 이중 반복문으로 모든 쌍을 확인하세요
    # ## 외부 반복문: i는 0부터 n-1까지
    # ## 내부 반복문: j는 i+1부터 n까지 (중복 방지)
    # ## nums[i] + nums[j]가 target과 같으면 (i, j)를 결과에 추가
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] + nums[j] == target:
    #             pairs.append((i,j))
    #return pairs

    ## 정석 풀이 말고 완전탐색 외의 풀이 방법 
    ## 서로 같은 원소가 여러개 일 때 조건을 추가해야 함.
    ## 예: nums = [1, 1, 1, 1], target = 2일 경우, (0,1), (0,2), (0,3), (1,2), (1,3), (2,3) 모두가 답이 됨
    ## 하지만 투 포인터 방식은 각각의 원소를 한 번씩만 사용하므로 중복을 방지함
    seen= defaultdict(list)
    for i,num in enumerate(nums):
        for j in seen[target-num]:
            pairs.append((j,i))
        seen[num].append(i)
    return pairs 
    
    
            
    # 이중 포문과 투 포인터 방식의 시간복잡도와 공간복잡도 비교 
    ## 이중 포문: 시간복잡도 O(n^2), 공간복잡도 O(1)
    ## 투 포인터: 시간복잡도 O(nlogn) (정렬 때문에), 공간복잡도 O(n) (정렬된 배열을 위한 추가 공간)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = find_two_sum_pairs(nums1, target1)
    print(f"배열: {nums1}")
    print(f"목표 합: {target1}")
    print(f"결과 쌍: {result1}")
    print()
    
    # 테스트 케이스 2
    nums2 = [1, 3, 4, 2, 5, 6]
    target2 = 7
    result2 = find_two_sum_pairs(nums2, target2)
    print(f"배열: {nums2}")
    print(f"목표 합: {target2}")
    print(f"결과 쌍: {result2}")
    print()
    
    # 테스트 케이스 3
    nums3 = [1, 1, 1, 1]
    target3 = 2
    result3 = find_two_sum_pairs(nums3, target3)
    print(f"배열: {nums3}")
    print(f"목표 합: {target3}")
    print(f"결과 쌍: {result3}")



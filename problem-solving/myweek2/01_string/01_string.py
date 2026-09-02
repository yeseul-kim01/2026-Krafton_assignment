"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""
#모든 문자열의 공백이랑 특수문자를 지운 후 반으로 나누기
# 개수가 홀수개일 경우 중간자리 빼고 반으로 나누기
# 반으로 나눈 다음 그 뒷 문장을 별개의 String list 로 저장한 뒤에 
# reserve 시키고 서로 같을 시 True 다른 String일시 False 반환 동등 연산자를 통해서 

def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # # 첫번째 풀이 
    # s = ''.join(e for e in s if e.isalnum()).lower()
    # print(s)
    
    # # 반으로 나눈거 끼리 비교하기
    # len_s= len(s)
    # if len(s)%2 ==0: 
    #     if s[:len_s//2] == s[len_s//2:][::-1]:
    #         return True
    #     else:
    #         return False
    # else:
    #     if s[:len_s//2] == s[len_s//2+1:][::-1]:
    #         return True
    #     else:
    #         return False
        
    # 두번째 풀이 
    ## 짧코
    s = ''.join(filter(str.isalnum, s)).lower()
    # filter 함수 설명하기
    # filter(function, iterable) 함수는 iterable(반복 가능한 객체)의 각 요소에 대해 function(함수)을 적용하여 True를 반환하는 요소만 걸러내는 역할
    return s == s[::-1]

    ## 람다 함수를 이용한 풀이 
    # s = ''.join(filter(lambda x: x.isalnum(), s)).lower()
    # return s == s[::-1]
    
    # 세가지 풀이에 대한 시간 복잡도 및 공간 복잡도
    # 첫번째 풀이는 문자열을 정제하는 과정에서 O(n) 시간 복잡도를 가지며, 반으로 나누어 비교하는 과정에서도 O(n/2) 시간 복잡도를 가지므로 전체적으로 O(n) 시간 복잡도를 가집니다. 공간 복잡도는 정제된 문자열을 저장하기 위해 O(n)입니다.
    # 두번째 풀이는 filter와 join을 사용하여 문자열을 정제하는 과정에서 O(n) 시간 복잡도를 가지며, 문자열을 뒤집어 비교하는 과정에서도 O(n) 시간 복잡도를 가지므로 전체적으로 O(n) 시간 복잡도를 가집니다. 공간 복잡도는 정제된 문자열을 저장하기 위해 O(n)입니다.
    # 세번째 풀이는 람다 함수를 사용하여 문자열을 정제하는 과정에서 O(n) 시간 복잡도를 가지며, 문자열을 뒤집어 비교하는 과정에서도 O(n) 시간 복잡도를 가지므로 전체적으로 O(n) 시간 복잡도를 가집니다. 공간 복잡도는 정제된 문자열을 저장하기 위해 O(n)입니다.
    #return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = " 1 "
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")



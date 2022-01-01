def solution(a, b):
    # 1. 등차수열 공식 이용 : 가장 효율적
    # - 등차수열 공식 : Sn = n * (a + l) / 2
    n = abs(a - b) + 1
    answer = n * ( a + b ) / 2
    
    
    # 2, 3 번 풀이의 경우, 일부 테스트 케이스(배열의 크기가 큰 경우)에서 시간소모가 큼
    
    # 2. for 문 이용
    # total = 0
    # for i in range(min(a,b), max(a,b) + 1):
    #     total += i
    # answer = total
    
    # 3. 바로 리스트 생성 + sum() 메소드 이용
    # arr = list(range(min(a,b), max(a,b) + 1))
    # answer = sum(arr)
    
    return answer
def solution(x, n):
    # 1. 등차 수열 이용 코드
    # - 등차 수열 : An = a + d(n-1)
    #   - 여기서 a = d -> An = a * n
    # answer = []
    # for i in range(1, n + 1):
    #     answer.append(x * i)
    
    # 2. 빠른 코드
    # - x = 0일 때, 고려해줘야 함!
    if x != 0:
        answer = list(range(x, x*(n+1), x))
    else:
        answer = [0] * n
    return answer
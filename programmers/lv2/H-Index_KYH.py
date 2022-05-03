def solution(citations):
    n = len(citations)
    citations.sort()
    
    for i in range(n):
        # h번 이상 인용된 논문이 h편 이상 조건
        if citations[i] >= n - i:  # n - i : 인용된 논문의 수의 갯수를 최댓값(n)부터 비교
            return  n - i
    return 0 # 얘 있고없고 차이점?
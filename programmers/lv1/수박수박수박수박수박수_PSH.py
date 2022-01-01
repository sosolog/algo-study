def solution(n):
    time = n // 2
    remain = n % 2
    answer = '수박' * time
    if remain == 1:
        answer += '수'
    return answer
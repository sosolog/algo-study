def solution(n):
    answer = 0
    new = str(n)
    for i in range(len(new)):
        answer += int(new[i])
    return answer
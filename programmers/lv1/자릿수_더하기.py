def solution(n):
    text = str(n)
    
    answer = 0
    for i in range(len(text)):
        answer += int(text[i])
    return answer

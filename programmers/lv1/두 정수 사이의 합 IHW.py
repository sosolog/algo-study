def solution(a, b):
    answer = 0
    i=0
    if a >= b:
        for i in range(b, a + 1):
            answer += i
            i+=1
    else:
        for i in range(a, b + 1):
            answer += i
            i+=1

    return answer

# 이중 for문
def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            if(prices[i]>prices[j]):
                sec += 1
                break
            else:
                sec += 1
        answer.append(sec)
    return answer
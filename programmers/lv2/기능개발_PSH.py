import math

def solution(progresses, speeds):
    stack = []
    answer = []
    for i in range(len(progresses)):
        remains = math.ceil((100 - progresses[i])/speeds[i])
        if len(stack) == 0 or stack[-1] < remains :
            stack.clear()
            stack.append(remains)
            answer.append(1)
        elif stack[-1] >= remains: 
            answer[-1] += 1
    
    return answer
  
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)

def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while len(stack)!=0 and prices[stack[-1]] > prices[i]:
            answer[stack[-1]] = i - stack[-1]
            del stack[-1]
        
        stack.append(i)
    
    for i in stack:
        answer[i] = len(prices) -1 - i    
    
    return answer
  
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.30ms, 10.3MB)
# 테스트 4 〉	통과 (0.35ms, 10.3MB)
# 테스트 5 〉	통과 (0.44ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.22ms, 10.2MB)
# 테스트 8 〉	통과 (0.26ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.42ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (36.73ms, 18.9MB)
# 테스트 2 〉	통과 (28.62ms, 17.6MB)
# 테스트 3 〉	통과 (40.73ms, 19.6MB)
# 테스트 4 〉	통과 (32.24ms, 18.3MB)
# 테스트 5 〉	통과 (22.63ms, 17MB)

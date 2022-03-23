from collections import deque

def solution(people, limit):
    people.sort()
    people_list = deque(people)
    
    answer = 0
    while len(people_list) > 1:
        if people_list[0] + people_list[-1] <= limit:
            people_list.pop()
            people_list.popleft()
        else:
            people_list.pop()
        answer += 1
    if len(people_list) == 1:
        answer += 1
    return answer
  
# 정확성  테스트
# 테스트 1 〉	통과 (1.00ms, 10.4MB)
# 테스트 2 〉	통과 (0.86ms, 10.1MB)
# 테스트 3 〉	통과 (0.72ms, 10.2MB)
# 테스트 4 〉	통과 (0.71ms, 10.2MB)
# 테스트 5 〉	통과 (0.42ms, 10.2MB)
# 테스트 6 〉	통과 (0.24ms, 10.2MB)
# 테스트 7 〉	통과 (0.36ms, 10.1MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.4MB)
# 테스트 10 〉	통과 (0.71ms, 10.2MB)
# 테스트 11 〉	통과 (0.58ms, 10.1MB)
# 테스트 12 〉	통과 (0.54ms, 10.3MB)
# 테스트 13 〉	통과 (0.70ms, 10.3MB)
# 테스트 14 〉	통과 (0.96ms, 10.2MB)
# 테스트 15 〉	통과 (0.09ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.50ms, 10.7MB)
# 테스트 2 〉	통과 (11.11ms, 10.8MB)
# 테스트 3 〉	통과 (10.76ms, 10.7MB)
# 테스트 4 〉	통과 (12.54ms, 10.7MB)
# 테스트 5 〉	통과 (11.01ms, 10.7MB)

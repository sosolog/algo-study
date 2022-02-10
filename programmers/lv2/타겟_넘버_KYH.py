from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0],0])
    q.append([-1*numbers[0],0])
    while q:
        sum, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([sum+numbers[idx], idx])
            q.append([sum-numbers[idx], idx])
        else:
            if sum == target:
                answer += 1
    return answer
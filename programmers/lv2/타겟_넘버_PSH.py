from collections import deque

def solution(numbers, target):
    s = deque()
    s.append(0)
    depth_num = 1
	
    for i in range(len(numbers)):
        num, depth_num = depth_num, 0
        for j in range(num):
            temp = s.popleft()
            s.append(temp + numbers[i])
            s.append(temp - numbers[i])
            depth_num += 2

    answer = 0
    for i in range(len(s)):
        if s.popleft() == target:
            answer += 1

    return answer

from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(p,l) for l,p in enumerate(priorities)])   
    # q = deque([(2, 0), (1, 1), (3, 2), (2, 3)])

    while q:
        temp = q.popleft()
        if q and max(q)[0] > temp[0]: # q가 비는 경우 max함수도 비어 버리므로 q의 존재 조건 추가
            q.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer

print(solution([2, 1, 3, 2],2))
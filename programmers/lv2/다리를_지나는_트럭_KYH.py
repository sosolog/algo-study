from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    while bridge:
        answer += 1
        bridge.popleft()
        if truck_weights:
            if(sum(bridge) + truck_weights[0]) <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (13.04ms, 10.2MB)
테스트 2 〉	통과 (1831.97ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (368.38ms, 10.2MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (2088.36ms, 10.3MB)
테스트 7 〉	통과 (6.57ms, 10.2MB)
테스트 8 〉	통과 (0.26ms, 10.2MB)
테스트 9 〉	통과 (10.66ms, 10.2MB)
테스트 10 〉	통과 (0.44ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.48ms, 10.2MB)
테스트 13 〉	통과 (1.91ms, 10.4MB)
테스트 14 〉	통과 (0.01ms, 10.4MB)
'''



from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    while bridge:
        answer += 1
        bleft = bridge.popleft()
        bridge_weight -= bleft
        if truck_weights:
            if(bridge_weight + truck_weights[0]) <= weight:
                twleft = truck_weights.popleft()
                bridge.append(twleft)
                bridge_weight += twleft
            else:
                bridge.append(0)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.41ms, 10.3MB)
테스트 2 〉	통과 (7.25ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (5.79ms, 10.3MB)
테스트 5 〉	통과 (55.50ms, 10.3MB)
테스트 6 〉	통과 (15.74ms, 10.3MB)
테스트 7 〉	통과 (0.59ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.2MB)
테스트 9 〉	통과 (2.01ms, 10.3MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.24ms, 10.3MB)
테스트 13 〉	통과 (0.54ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
'''
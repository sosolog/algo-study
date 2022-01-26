def solution(bridge_length, weight, truck_weights):
    temp_time = 1
    timer = [temp_time+bridge_length]
    bridge = [truck_weights.pop(0)]
    temp_time+= 1
    
    while len(timer) > 0:
        if timer[0] == temp_time:
            bridge.pop(0)
            timer.pop(0)
       
        if len(truck_weights) != 0 and weight - sum(bridge) >= truck_weights[0]:
            bridge.append(truck_weights.pop(0))
            timer.append(temp_time+bridge_length)
            
        if (len(truck_weights) != 0 and weight - sum(bridge) < truck_weights[0]) or (len(truck_weights) == 0 and len(bridge) != 0):
            temp_time = timer[0]
            continue
        
        temp_time += 1
        
    return temp_time -1
 
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.58ms, 10.3MB)
# 테스트 5 〉	통과 (0.67ms, 10.2MB)
# 테스트 6 〉	통과 (1.07ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.40ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.00ms, 10.3MB)

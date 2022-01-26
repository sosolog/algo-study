def solution(answers):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i in range(len(answers)):
        if arr1[i%len(arr1)] == answers[i] : count[0] += 1
        if arr2[i%len(arr2)] == answers[i] : count[1] += 1
        if arr3[i%len(arr3)] == answers[i] : count[2] += 1
    
    answer = []
    max_num = max(count)
    for i in range(len(count)):
        if count[i] == max_num : answer.append(i+1)
    return answer
    
    
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (1.78ms, 10.3MB)
# 테스트 8 〉	통과 (0.57ms, 10.4MB)
# 테스트 9 〉	통과 (3.15ms, 10.3MB)
# 테스트 10 〉	통과 (1.48ms, 10.3MB)
# 테스트 11 〉	통과 (3.36ms, 10.3MB)
# 테스트 12 〉	통과 (2.92ms, 10.4MB)
# 테스트 13 〉	통과 (0.18ms, 10.2MB)
# 테스트 14 〉	통과 (3.54ms, 10.3MB)

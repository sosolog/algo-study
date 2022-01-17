def solution(progresses, speeds):
    answer = []
    workDay = []
    for i in range(len(progresses)):
        day = 0
        while(progresses[i]+speeds[i]*day < 100):
            day += 1
        workDay.append(day)
        
    count = 1
    idx = workDay[0]
    for i in range(1, len(workDay)):
        if idx >= workDay[i]:
            count += 1
        else:
            answer.append(count)
            idx = workDay[i]
            count = 1
    answer.append(count)
        
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.17ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉통과 (0.08ms, 10.3MB)
테스트 11 〉통과 (0.01ms, 10.3MB)
'''
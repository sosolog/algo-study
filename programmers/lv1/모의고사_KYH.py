def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    
    for i in range(len(answers)):
        i1 = i % len(p1)
        i2 = i % len(p2)
        i3 = i % len(p3)
        
        if(p1[i1] == answers[i]):
            score[0] += 1
        if(p2[i2] == answers[i]):
            score[1] += 1
        if(p3[i3] == answers[i]):
            score[2] += 1
    
    for j in range(len(score)):
        if(score[j] == max(score)):
            answer.append(j+1)
    return answer
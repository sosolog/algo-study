def solution(s):
    answer = True
    lower_s = s.lower()
    count_p = 0
    count_y = 0
    
    for i in range(len(s)):
        if(lower_s[i] == 'p'):
            count_p += 1
        elif(lower_s[i] == 'y'):
            count_y += 1
    if(count_p != count_y):
        answer = False
    return answer
def solution(s):
    answer = True
    p = y = 0
    for i in range(len(s)):
        if s[i].lower()=='p':
            p += 1
        elif s[i].lower()=='y':
            y += 1
    if p != y:
        answer = False   
    
    return answer
def solution(s):
    i = 0
    answer = ''
    count = 0
    for i in range(i,len(s)):
        if s[i] == ' ':
            count = 0
            answer += s[i]
            
        elif (count % 2) == 0:
            answer += s[i].upper()
            count += 1
            
        else:
            answer += s[i].lower()
            count += 1

    return answer
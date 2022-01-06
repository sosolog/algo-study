def solution(s):
    strArr = s.split(' ')
    answer = ''
    for text in strArr:
        for i in range(len(text)):
            if(i % 2 == 0):
                answer += text[i].upper()
            else:
                answer += text[i].lower()
        answer += ' '
    return answer[:len(answer)-1]
from collections import deque

def conversion(p):
    if p == '(':
        return ')'
    if p == ')':
        return '('
    return ""

def solution(text):
    if len(text) == 0:
        return ""
    stack = deque()
    check = True
    idx = 0
    flag = 0
    
    while True:
        t = text[idx]
        if t == "(":
            flag += 1
            stack.append('(')
        else:
            flag -= 1
            if len(stack) == 0:
                check = False
            else:
                stack.pop()
                
        if flag == 0:
            break
        idx += 1
        
    if check:
        return text[:idx+1] + solution(text[idx+1:])
    else:
        text_converse = "".join(list(map(conversion, text[1:idx])))
        return "(" + solution(text[idx+1:]) + ")" + solution(text_converse)
      
# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.05ms, 10.4MB)
# 테스트 14 〉	통과 (0.07ms, 10.3MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 테스트 16 〉	통과 (0.22ms, 10.2MB)
# 테스트 17 〉	통과 (0.16ms, 10.3MB)
# 테스트 18 〉	통과 (0.23ms, 10.2MB)
# 테스트 19 〉	통과 (0.66ms, 10.4MB)
# 테스트 20 〉	통과 (0.31ms, 10.2MB)
# 테스트 21 〉	통과 (0.38ms, 10.2MB)
# 테스트 22 〉	통과 (0.20ms, 10.3MB)
# 테스트 23 〉	통과 (0.27ms, 10.2MB)
# 테스트 24 〉	통과 (0.10ms, 10.3MB)
# 테스트 25 〉	통과 (0.14ms, 10.2MB)

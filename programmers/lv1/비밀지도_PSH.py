def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num = arr1[i] | arr2[i]
        answer.append(binary(num).rjust(n, ' '))
    return answer

def binary(n):
    number = ''
    while True:
        remain = ' ' if n % 2 == 0 else '#' 
        n = n // 2
        number = remain + number
        if n == 0 : break
    return number
    
# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.07ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)

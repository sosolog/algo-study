def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer
  
#   정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 9.97MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)

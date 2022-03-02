def solution(participant, completion):
    dict = {}
    for p in completion:
        if dict.get(p) == None:
            dict[p] = 1
        else:
            dict[p] += 1
    
    for p in participant:
        if dict.get(p) == None:
            return p
        elif dict[p] > 0:
            dict[p] -= 1
        elif dict[p] == 0:
            return p
    return ''
  
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.19ms, 10.3MB)
# 테스트 4 〉	통과 (0.29ms, 10.2MB)
# 테스트 5 〉	통과 (0.29ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (24.53ms, 21.6MB)
# 테스트 2 〉	통과 (36.50ms, 25.1MB)
# 테스트 3 〉	통과 (30.58ms, 27.6MB)
# 테스트 4 〉	통과 (34.23ms, 33.9MB)
# 테스트 5 〉	통과 (61.11ms, 33.9MB)

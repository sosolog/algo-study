def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.08ms, 10.3MB)
# 테스트 3 〉	통과 (0.28ms, 10.3MB)
# 테스트 4 〉	통과 (0.25ms, 10.3MB)
# 테스트 5 〉	통과 (0.10ms, 10.3MB)
# 테스트 6 〉	통과 (0.15ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.08ms, 10.3MB)
# 테스트 9 〉	통과 (1.16ms, 11MB)
# 테스트 10 〉	통과 (0.73ms, 10.8MB)
# 테스트 11 〉	통과 (0.53ms, 10.5MB)
# 테스트 12 〉	통과 (0.62ms, 10.7MB)
# 테스트 13 〉	통과 (0.70ms, 10.5MB)
# 테스트 14 〉	통과 (0.58ms, 10.6MB)
# 테스트 15 〉	통과 (0.69ms, 10.7MB)
# 테스트 16 〉	통과 (0.59ms, 10.6MB)
# 테스트 17 〉	통과 (31.77ms, 22.9MB)

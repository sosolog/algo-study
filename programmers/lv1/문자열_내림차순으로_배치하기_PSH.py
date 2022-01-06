def solution(s):
    arr = sorted(s)
    arr.reverse()
    
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer
def solution(arr):
    for i in range(1, len(arr)):
        a = max(arr[i-1], arr[i])
        b = min(arr[i-1], arr[i])
        arr[i] = LCM(a, b)   
    answer = arr[len(arr) - 1]
    return answer

def GCD(a, b):
    result = a
    while result != 0:
        result = a % b
        a = b
        b = result
    return a

def LCM(a, b):
    return a * b / GCD(a, b)
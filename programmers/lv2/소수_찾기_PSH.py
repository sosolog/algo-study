import itertools
import math

def solution(numbers):
    arr = []
    for char in numbers:
        arr.append(char)
    number = []
    for i in range(1, len(arr)+1):
        number += list(map(''.join, itertools.permutations(arr, i)))
    # print(number)
    number = set(map(int, number))
    # print(number)
    
    prime_arr = prime(numbers)
    
    answer =0
    for num in number:
        if prime_arr[num]: answer+=1
    return answer

def prime(num) :
    arr = [True for _ in range(pow(10,len(num)))]
    arr[0] = False
    arr[1] = False
    for i in range(2,len(arr)):
        if arr[i]: 
            for j in range(2, math.ceil(len(arr)/i)):
                if arr[i*j]: arr[i*j]= False
    return arr
  
#  정확성  테스트
# 테스트 1 〉	통과 (2.63ms, 10.5MB)
# 테스트 2 〉	통과 (303.01ms, 18.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.5MB)
# 테스트 4 〉	통과 (296.13ms, 18.1MB)
# 테스트 5 〉	통과 (4301.59ms, 87.4MB)
# 테스트 6 〉	통과 (0.08ms, 10.4MB)
# 테스트 7 〉	통과 (2.63ms, 10.5MB)
# 테스트 8 〉	통과 (4312.23ms, 87.3MB)
# 테스트 9 〉	통과 (0.27ms, 10.4MB)
# 테스트 10 〉	통과 (469.14ms, 18.2MB)
# 테스트 11 〉	통과 (34.88ms, 11.3MB)
# 테스트 12 〉	통과 (44.45ms, 11.3MB)

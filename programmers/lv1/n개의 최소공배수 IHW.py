def solution(arr):
    from math import gcd   # 최소공약수 쓰기위함 
    answer = arr[0]    # 배열의 첫 숫자부터 시작 

    for i in arr: # 배열 하나씩 호출 
        answer = answer * i // gcd(answer,i)   # 최소 공배수 공식 =        두 수의 곱 / 두 수의 최소공약수
    return answer
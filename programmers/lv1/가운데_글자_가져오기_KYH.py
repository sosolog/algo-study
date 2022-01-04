def solution(s):
    answer = ''
    a = list(str(s))
    if len(s) % 2 == 0:
        answer = a[len(a)//2-1]+a[len(a)//2]
    else:
        answer = a[len(a)//2]
    return answer
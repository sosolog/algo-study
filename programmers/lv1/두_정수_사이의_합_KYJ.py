<<<<<<< HEAD
def solution(a, b):
    answer = 0
    if a==b:
        return a
    elif a<b:
        for i in range(a,b+1):
            answer+=i
    elif a>b:
        for i in range(b,a+1):
            answer+=i
    return answer
=======
def solution(a, b):
    answer = 0
    if a==b:
        return a
    elif a<b:
        for i in range(a,b+1):
            answer+=i
    elif a>b:
        for i in range(b,a+1):
            answer+=i
    return answer
>>>>>>> 22d3d7ce4f5b62a2e8db5eee402ab8ca95620766

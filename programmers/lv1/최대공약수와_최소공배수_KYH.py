def gcd(a, b):
    if(a>b):
        temp = b
        b = a
        a = temp
    while(1):
        if(b%a == 0):
            return a
            break
        else:
            c = b%a
            b = a
            a = c

def solution(n, m):
    answer = [gcd(n, m), n*m/gcd(n, m)]
    return answer
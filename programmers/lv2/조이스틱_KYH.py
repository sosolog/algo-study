def solution(name):
    UpDown = 0
    LeftRight = len(name) - 1
    
    for i, n in enumerate(name):
        if ord(n) > 78:
            UpDown += (91 - ord(n))
        else:
            UpDown += (ord(n) - 65)
            
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        LeftRight = min(LeftRight, 2 * i + (len(name) - next), i + 2 * (len(name) - next))
    return UpDown + LeftRight
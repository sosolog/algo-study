def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            count += 1
        elif s[i] == 'y' or s[i] == 'Y':
            count -= 1
    return True if count == 0 else False
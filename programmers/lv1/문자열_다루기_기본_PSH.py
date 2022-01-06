def solution(s):
    number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    if len(s) != 4 and len(s) != 6:
        return False

    for i in range(len(s)):
        if s[i] not in number:
            return False
    return True
def solution(name):
    if name.count('A') == len(name):
        return 0
    else:
        count = 0
        for char in name:
            count += min(ord(char)-ord('A'), ord('Z')+1-ord(char))

        idx = name.find('A')
        if idx < 0:
            count += len(name) - 1
        else:
            candid = list()
            while idx >= 0:
                x = name[:idx].rstrip('A')
                y = name[idx:].lstrip('A')
                x_len = len(x)-1 if len(x) != 0 else 0
                y_len = len(y)
                candid.append(min(x_len*2 + y_len, x_len + y_len*2))
                if idx == len(name) - 1:
                    break
                idx = name.find('A', idx+1)
            candid.append(len(name) - 1)
            count += min(candid)
    return count
  
#   정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 테스트 17 〉	통과 (0.00ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (0.03ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.3MB)
# 테스트 22 〉	통과 (0.02ms, 10.3MB)
# 테스트 23 〉	통과 (0.02ms, 10.1MB)
# 테스트 24 〉	통과 (0.02ms, 10.4MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
# 테스트 26 〉	통과 (0.02ms, 10.2MB)
# 테스트 27 〉	통과 (0.02ms, 10.2MB)

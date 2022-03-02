def solution(phone_book):
    lengths = set()
    for phone in phone_book:
        lengths.add(len(phone))
    for length in sorted(lengths):
        dict = {}
        for phone in sorted(phone_book, key=len):
            if len(phone) == length:
                dict[phone] = True
            elif len(phone) > length:
                if dict.get(phone[:length]):
                    return False
    return True
 
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (2.81ms, 10.3MB)
# 테스트 15 〉	통과 (3.46ms, 10.3MB)
# 테스트 16 〉	통과 (0.45ms, 10.4MB)
# 테스트 17 〉	통과 (0.94ms, 10.3MB)
# 테스트 18 〉	통과 (4.35ms, 10.3MB)
# 테스트 19 〉	통과 (1.41ms, 10.3MB)
# 테스트 20 〉	통과 (3.23ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1.83ms, 10.9MB)
# 테스트 2 〉	통과 (1.78ms, 11MB)
# 테스트 3 〉	통과 (61.56ms, 48MB)
# 테스트 4 〉	통과 (47.95ms, 31MB)

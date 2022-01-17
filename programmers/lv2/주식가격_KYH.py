# 이중 for문
def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            if(prices[i]>prices[j]):
                sec += 1
                break
            else:
                sec += 1
        answer.append(sec)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (1.10ms, 10.3MB)
테스트 4 〉	통과 (0.66ms, 10.4MB)
테스트 5 〉	통과 (0.86ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.38ms, 10.3MB)
테스트 8 〉	통과 (0.90ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉통과 (1.55ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (122.11ms, 18.9MB)
테스트 2 〉	통과 (94.61ms, 17.6MB)
테스트 3 〉	통과 (135.46ms, 19.6MB)
테스트 4 〉	통과 (98.01ms, 18.2MB)
테스트 5 〉	통과 (74.74ms, 17.1MB)
'''

# 큐
# collections 모듈의 deque는 double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices: # popleft로 다 빠지면 prices가 false
        sec = 0
        pleft = prices.popleft()
        for i in prices:
            if (pleft > i):
                sec += 1
                break
            else:
                sec += 1
        answer.append(sec)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.29ms, 10.3MB)
테스트 4 〉	통과 (0.31ms, 10.3MB)
테스트 5 〉	통과 (0.46ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.34ms, 10.3MB)
테스트 8 〉	통과 (0.23ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉통과 (0.39ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (60.26ms, 18.9MB)
테스트 2 〉	통과 (47.01ms, 17.6MB)
테스트 3 〉	통과 (68.03ms, 19.5MB)
테스트 4 〉	통과 (48.47ms, 18.2MB)
테스트 5 〉	통과 (36.04ms, 17MB)
'''
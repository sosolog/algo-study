import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        heapq.heappush(scoville, mix)
        count += 1
    if heapq.heappop(scoville) >= K:
        return count
    return -1
  
#  정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.43ms, 10.2MB)
# 테스트 7 〉	통과 (0.64ms, 9.94MB)
# 테스트 8 〉	통과 (0.09ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10MB)
# 테스트 10 〉	통과 (0.29ms, 10.3MB)
# 테스트 11 〉	통과 (0.18ms, 10.2MB)
# 테스트 12 〉	통과 (0.68ms, 10.2MB)
# 테스트 13 〉	통과 (0.38ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.48ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (175.96ms, 16.3MB)
# 테스트 2 〉	통과 (387.51ms, 22MB)
# 테스트 3 〉	통과 (1725.32ms, 49.7MB)
# 테스트 4 〉	통과 (146.09ms, 14.9MB)
# 테스트 5 〉	통과 (1891.17ms, 51.7MB)
 

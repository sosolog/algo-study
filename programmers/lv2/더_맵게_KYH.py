import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        new_food = heapq.heappop(scoville) + (2 * heapq.heappop(scoville))
        heapq.heappush(scoville, new_food)
    if scoville[0] < K:
        answer = -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))

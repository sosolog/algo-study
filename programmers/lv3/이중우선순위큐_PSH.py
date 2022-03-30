import heapq

def solution(operations):
    heap = []
    for operation in operations:
        op, data = operation.split()
        if op == 'I':
            heapq.heappush(heap, int(data))
        elif op == 'D' and data == '1':
            if len(heap) > 0:
                heap.pop()
        else:
            if len(heap) > 0:
                heapq.heappop(heap)
        # print(heap)
            
    if len(heap) == 0:
        return [0,0]
    return [max(heap), min(heap)]
  
#   정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.5MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)

import heapq

def solution(operations):
    heap = []

    for o in operations:
        order, data = o.split()
        data = int(data)
        if order == "D" and data == 1:
            if heap:
                max_heap = max(heap)
                heap.remove(max_heap)
        elif order == "D" and data == -1:
            if heap:
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, data)
    if not heap:
        return [0,0]
    return [max(heap), heap[0]]

print(solution(["I 16","D 1"]))
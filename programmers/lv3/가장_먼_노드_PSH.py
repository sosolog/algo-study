from collections import deque

def solution(n, edge):
    rmap = dict()
    for (point1, point2) in edge: 
        if not point1 in rmap:
            rmap[point1] = list() 
        if not point2 in rmap:
            rmap[point2] = list() 
        rmap[point1].append(point2) 
        rmap[point2].append(point1)
    

    visited = [False for _ in range(n+1)]
    price = [2**31-1 for _ in range(n+1)]
    
    visited[0] = True
    price[0] = -1

    start = 1
    price[start] = 0
    
    q = deque()
    q.append(start)
    
    while len(q) > 0:
        start = q.popleft()
        if not visited[start]:
            visited[start] = True
            candidates = rmap.get(start)

            if candidates:
                for candid in candidates:
                    if not visited[candid]:
                        cand_price = price[start] + 1  
                        price[candid] = min(price[candid], cand_price)
                        q.append(candid)
        
    max_val = max(price)
    count = 0
    for p in price:
        if p == max_val:
            count += 1
    
    return count
  
#  정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.34ms, 10.2MB)
# 테스트 5 〉	통과 (1.54ms, 10.4MB)
# 테스트 6 〉	통과 (3.83ms, 10.9MB)
# 테스트 7 〉	통과 (33.36ms, 17.5MB)
# 테스트 8 〉	통과 (60.77ms, 21.2MB)
# 테스트 9 〉	통과 (60.86ms, 20.7MB)

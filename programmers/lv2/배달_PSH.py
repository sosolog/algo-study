def solution(N, road, K):
    # 현재 point과 바로 연결된 point의 후보군 모으는 dictionary
    # key: point, value: list형태[요소 : 튜플(연결 point, 걸리는 시간)]
    rmap = dict()
    for point in range(1, N+1): 
        # 각 point(1~N)의 연결 point 후보군을 담을 list 생성
        rmap[point] = list()

    for (point1, point2, price) in road: 
        # (연결 point, 걸리는 시간)을 각 point의 후보군 list 내 담기
        rmap[point1].append((point2,price)) # point1 기준 시각
        rmap[point2].append((point1,price)) # point2 기준 시각
    

    visited = [False for _ in range(N)] # 갔다온 곳 체크 list
    price = [2**31-1 for _ in range(N)] # (시작 => 해당 point)까지 걸리는 시간 담는 list

    start = 1           # 시작점
    price[start-1] = 0  # 시작점=>시작점, 걸리는 시간 = 0
    
    while False in visited:         # 모든 point가 True가 되면[모든 point 방문했을 시] 반복문 탈출
        visited[start-1] = True     # 현재 point 방문했다고 표시
        candidates = rmap[start]    # 현재 point 기준 바로 연결된 point 후보군 리스트
        for candi in candidates:    # candi => (연결된 point, 걸리는 시간)
            point = candi[0]        # 연결된 point
            point_value = candi[1]  # (현재 => 연결 point)까지 걸리는 시간
            if not visited[point-1]:                        # 연결된 point 중 방문 안한 곳
                cand_price = price[start-1] + point_value   # (시작점 => 현재 point)까지 걸리는 시간 + (현재 => 연결 point)까지 걸리는 시간 
                price[point-1] = min(price[point-1], cand_price) # (시작점=>연결 point)까지 걸리는 시간

        min_p = 0           # (시작 => 특정 point)까지 걸리는 시간이 최솟값을 가진 point
        min_v = 2**31-1     # (시작 => 특정 point)까지 걸리는 시간의 최솟값
        for i in range(1,N+1):
            if not visited[i-1] and min_v > price[i-1]: 
                min_p = i 
                min_v = price[i-1]

        start = min_p  # 현재 방문하지 않은 point 중, (시작=>특정) 걸리는 시간의 최소인 곳...
    
    # 시작 => 특정 까지의 걸리는 최적 시간을 담은 list[변수명 : price] 완성 후,
    count = 0
    for p in price: # 걸리는 시간이 기준 시간 보다 같거나 작은 개수 세기
        if p <= K: 
            count += 1
    
    return count
  
#  정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.5MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.14ms, 10.3MB)
# 테스트 13 〉	통과 (0.11ms, 10.4MB)
# 테스트 14 〉	통과 (0.75ms, 10.5MB)
# 테스트 15 〉	통과 (1.03ms, 10.5MB)
# 테스트 16 〉	통과 (0.07ms, 10.3MB)
# 테스트 17 〉	통과 (0.09ms, 10.3MB)
# 테스트 18 〉	통과 (0.37ms, 10.3MB)
# 테스트 19 〉	통과 (1.01ms, 10.6MB)
# 테스트 20 〉	통과 (0.38ms, 10.4MB)
# 테스트 21 〉	통과 (1.23ms, 10.6MB)
# 테스트 22 〉	통과 (0.46ms, 10.4MB)
# 테스트 23 〉	통과 (1.22ms, 10.6MB)
# 테스트 24 〉	통과 (0.97ms, 10.5MB)
# 테스트 25 〉	통과 (3.03ms, 10.6MB)
# 테스트 26 〉	통과 (1.78ms, 10.6MB)
# 테스트 27 〉	통과 (1.84ms, 10.7MB)
# 테스트 28 〉	통과 (1.92ms, 10.7MB)
# 테스트 29 〉	통과 (1.84ms, 10.8MB)
# 테스트 30 〉	통과 (3.62ms, 10.7MB)
# 테스트 31 〉	통과 (0.23ms, 10.3MB)
# 테스트 32 〉	통과 (0.29ms, 10.3MB)

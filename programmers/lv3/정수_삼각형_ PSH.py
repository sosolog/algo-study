# 하위 삼각형을 만들어서 넣지 말고 하위 삼각형의 꼭짓점을 넘기자!

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.09ms, 10MB)
# 테스트 4 〉	통과 (0.37ms, 10.1MB)
# 테스트 5 〉	통과 (2.83ms, 10.5MB)
# 테스트 6 〉	통과 (0.83ms, 10.2MB)
# 테스트 7 〉	통과 (2.85ms, 10.6MB)
# 테스트 8 〉	통과 (0.67ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10MB)
# 테스트 10 〉	통과 (0.35ms, 10.2MB)

# 효율성  테스트
# 테스트 1 〉	통과 (112.06ms, 32.2MB)
# 테스트 2 〉	통과 (84.52ms, 25.1MB)
# 테스트 3 〉	통과 (122.06ms, 33.9MB)
# 테스트 4 〉	통과 (110.38ms, 32.1MB)
# 테스트 5 〉	통과 (113.75ms, 32MB)
# 테스트 6 〉	통과 (137.42ms, 34.9MB)
# 테스트 7 〉	통과 (127.29ms, 32.8MB)
# 테스트 8 〉	통과 (104.34ms, 31.8MB)
# 테스트 9 〉	통과 (107.62ms, 32.1MB)
# 테스트 10 〉	통과 (115.24ms, 33.4MB)

# point => 현재 탐색 중인 하위삼각형의 꼭짓점(tuple 형식)
# memo => memoization을 위한 dictionary
# tri => 전체 삼각형 원본(2차원 배열형식) -> 주어진 데이터
def maxRoot(point, memo, tri):
	if len(tri) == 1: return tri[0][0]
	else:
		if point in memo:
			return memo[point]
		else:
			x = point[0] # 현재 탐색중인 삼각형의 꼭짓점 x 좌표
			y = point[1] # 현재 탐색중인 삼각형의 꼭짓점 y 좌표		
			if x < len(tri)-2 : # (len(tri)-1) : 삼각형 최하단 x 좌표 => len(tri)-2 : 삼각형 밑에서 두번째 줄 
				lChild_max = maxRoot((x+1, y), memo, tri) # 좌측 하단 자식 삼각형의 좌표 : (x+1, y)
				rChild_max = maxRoot((x+1, y+1), memo, tri) # 우측 하단 자식 삼각형의 좌표 : (x+1, y+1)
				memo[point] = max(lChild_max, rChild_max) + tri[x][y]
			else: #	현재 탐색중인 삼각형 꼭짓점이 삼각형 맨 밑에서 두번째 줄에 위치해 있을 때
				memo[point] = max(tri[x+1][y], tri[x+1][y+1]) + tri[x][y]				
			return memo[point]

case1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
mem = dict()
print(maxRoot((0,0), mem, case1))

def arithmetic(num_list1, num_list2, target, new):
	for i in num_list1:
		temp = set()
		for j in num_list2:
			temp.add(j + i)
			if i != j:
				minus = i - j if i > j else j - i
				temp.add(minus)
			temp.add(i * j)
			if i != 0 and j != 0:
				divide = i // j if i > j else j // i
				temp.add(divide)
		for j in temp:
			if j == target:
				return (True, None)
		new.update(temp)
	return (False, new)

def solution(N, number):
	if N == number:
		return 1
	memo = dict()
	memo[1] = set([N])
	memo[2] = set([int(str(N)*2), N+N, N*N, N//N]) # n-n == 0 이라서 생략
	for i in memo[2]:
		if i == number:
			return 2
	
	unit = {
		3:[(1,2)], 
		4:[(1,3), (2,2)], 
		5:[(1,4), (2,3)], 
		6:[(1,5), (2,4), (3,3)], 
		7:[(1,6),(2,5),(3,4)], 
		8:[(1,7), (2,6), (3,5), (4,4)]
	}
			
	for j in range(3,9):
		new = set()
		
		n_repeat = int(str(N)*j)
		if n_repeat == number: 
			return j
		new.add(n_repeat)
			
		for k in unit[j]:
			result = arithmetic(memo[k[0]], memo[k[1]], number, new)
			if result[0] :
				return j
				
		memo[j] = new
				
	return -1

# 정확성  테스트
# 테스트 1 〉	통과 (0.19ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.5MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (7.25ms, 10.9MB)
# 테스트 5 〉	통과 (1.92ms, 10.6MB)
# 테스트 6 〉	통과 (0.09ms, 10.5MB)
# 테스트 7 〉	통과 (0.10ms, 10.5MB)
# 테스트 8 〉	통과 (2.52ms, 10.5MB)
# 테스트 9 〉	통과 (0.00ms, 10.3MB)

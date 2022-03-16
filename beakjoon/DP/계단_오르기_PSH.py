# 30864	KB 68 ms

import sys

# 최대 점수 구하는 함수
def maxGrade(steps, memo): # steps => tuple형(계단별 점수 튜플), memo => dictionary형
	# print(memo) # memo 확인
	if len(steps) == 0: return 0
	elif len(steps) == 1: return steps[0]
	elif len(steps) == 2: return steps[0] + steps[1]
	else:
		if steps in memo:
			return memo[steps]
		else: # Sn = max( Sn-3 + an-1 + an, Sn-2 + an)
			value1 = maxGrade(steps[:-3], memo) + steps[-2] + steps[-1]
			value2 = maxGrade(steps[:-2], memo) + steps[-1]
			memo[steps] = max(value1, value2)
			return memo[steps]

# 계단 개수
stepNum = int(sys.stdin.readline().rstrip())

# 계단별 점수 확인
step = list()
for i in range(stepNum) :
	num = int(sys.stdin.readline().rstrip())
	step.append(num)
tup_step = tuple(step) # 계단별 점수(list)를 tuple로 변경
# print(tup_step) # 계단별 점수 확인

mem = dict() # memoization에 이용할 dictionary
result = maxGrade(tup_step, mem)
print(result)

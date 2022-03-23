#	30864 KB	72 ms

import sys

num = int(sys.stdin.readline().rstrip())
answer = [0, 0, 0]
unit = [5*60, 60, 10]

for i in range(3):
	answer[i] = num // unit[i]
	num = num % unit[i]

if num == 0:
	answer = list(map(str, answer))
	print(" ".join(answer))
else:
	print(-1)

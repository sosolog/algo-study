# 30860	KB 356 ms

import sys

factorial = {1:1, 2:2, 3:6, 4:24, 5:120}
while True:
	num = sys.stdin.readline().rstrip()
	if num == '0': break
	total = 0
	for i in range(len(num)):
		total += int(num[i]) * factorial[len(num)-i]
	print(total)

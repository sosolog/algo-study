# 	30860 KB	68 ms

def facto(num):
	if num == 0:
		return 1
	return facto(num-1) * num

num = int(input())
print(facto(num))

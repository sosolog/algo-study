def dec_to_bin(decimal):
	if decimal // 2 == 0:
		return str(decimal)
	bin_num = str(decimal % 2)
	return dec_to_bin(decimal // 2) + bin_num

num = int(input())
print(dec_to_bin(num))

# 	30864	KB  68 ms

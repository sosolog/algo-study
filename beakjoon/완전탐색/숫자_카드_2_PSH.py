# 115440 MB	/ 896 ms

x = int(input())
x_list = list(map(int, input().split()))
y = int(input())
y_list = list(map(int, input().split()))
x_dict = {}

for i in x_list:
    if x_dict.get(i) == None: x_dict[i] = 1
    else: x_dict[i] += 1

answer = [0 for _ in range(y)]

for i in range(y):
    if x_dict.get(y_list[i]) == None: answer[i] = 0
    else : answer[i] = x_dict.get(y_list[i])
print(*answer, sep=" ")

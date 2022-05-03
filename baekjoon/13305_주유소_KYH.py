import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
answer = 0
price = prices[0]

for i in range(N-1):
    if price >= prices[i]:
        price = prices[i]
    answer += price * roads[i]

print(answer)
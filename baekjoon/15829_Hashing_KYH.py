import sys
input = sys.stdin.readline

L = int(input())
r = 31
M = 1234567891
str = input()

temp = 0

for i in range(L):
    a = ord(str[i]) - 96
    temp += a * (r ** i)

H = temp % M
print(H)
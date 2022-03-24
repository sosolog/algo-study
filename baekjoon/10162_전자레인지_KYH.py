import sys
input = sys.stdin.readline

button_A = 300
button_B = 60
button_C = 10
T = int(input())

if T%10 != 0:
    print(-1)
else:
    A = T // button_A
    B = T % button_A // button_B
    C = T % button_A % button_B // button_C
    print(A,B,C)

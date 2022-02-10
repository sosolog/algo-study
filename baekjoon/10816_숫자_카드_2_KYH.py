import sys
input = sys.stdin.readline

M = int(input())
cards_M = list(map(int,input().split()))
cards_M.sort()
cardsDic = {}
for m in cards_M:
    if m not in cardsDic:
        cardsDic[m] = 1
    else:
        cardsDic[m] += 1

N = int(input())
cards_N = list(map(int,input().split()))

for n in cards_N:
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        if cards_M[mid] == n:
            break
        if cards_M[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
            
    if cards_M[mid] == n:
        print(cardsDic[n])
    else:
        print(0)

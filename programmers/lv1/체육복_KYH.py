def solution(n, lost, reserve):
    answer = n
    lost = set(lost)
    reserve = set(reserve)

    new_lost = lost - reserve
    new_reserve = reserve - lost
    
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    return answer-len(new_lost)


print(solution(5,[2, 4],[1, 3, 5]))
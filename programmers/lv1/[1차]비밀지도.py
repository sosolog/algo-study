def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        arr12 = bin(arr1[i] | arr2[i])
        arr12 = arr12[2:].zfill(n)
        arr12 = arr12.replace("1","#").replace("0"," ")
        answer.append(arr12)
    return answer
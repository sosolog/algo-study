from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [0 for _ in range(len(words))]

    while q:
        word, depth = q.popleft()
        if word == target:
            answer = depth
            break
        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append([words[i], depth + 1])
                    visited[i] = 1
    if depth == len(words):
        answer = 0

    return answer

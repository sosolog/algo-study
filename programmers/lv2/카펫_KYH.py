def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for height in range(1, total + 1):
        if total % height == 0:
            width = total / height
            if width >= height:
                if (height - 2) * (width - 2) == yellow:
                    answer = [width, height]
    return answer
def solution(phone_number):
    str_length = len(phone_number)
    front = '*' * (str_length - 4)
    answer = front + phone_number[str_length-4:]
    return answer
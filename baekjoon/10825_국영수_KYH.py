import sys
input = sys.stdin.readline


N = int(input())
students = []
for i in range(N):
    [name, kor, eng, math] = input().split()
    students.append([name, int(kor), int(eng), int(math)])

# sort lambda 함수  - : 내림차순
# list.sort(key=lambda x: (정렬대상))  or  sorted(list, key=lambda x: (정렬대상))
students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
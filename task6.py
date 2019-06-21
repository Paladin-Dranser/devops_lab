number_students, number_subjects = list(map(int, input().split()))

marks = []
for subject in range(number_subjects):
    marks.append(tuple(map(float, input().split())))

for mark_student in zip(*marks):
    print(sum(mark_student) / len(mark_student))

# elif문 전체 중 하나의 조건에 만족하면 나머지 if 문을 실행되지 않도록 작동
score = int(input("Write your score:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)

print("무슨 학교를 다니는지 알아보겠습니다.")
print("당신의 출생한 년도 입력해주세요:")
year = int(input())
age = (2019 - year) + 1

if age >= 20 and age <= 26:
    print("대학생 입니다.")
elif age >= 17 and age < 20:
    print(" 고등학생 입니다.")
elif age >=14 and age < 17:
    print("중학생 입니다.")
elif age >= 8 and age < 14:
    print("초등학생 입니다.")
else:
    print("학생이 아닙니다.")

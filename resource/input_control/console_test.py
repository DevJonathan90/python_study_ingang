"""print("Enter your name:")
somebody = input()
print ("Hi", somebody, "How are you today?")
"""

# input() 함수는 항상 str로 값을 받는다.
temperature = input("온도를 입력하세요:")
print(type(temperature))

temperature = float(input("온도를 입력하세요:"))
print(type(temperature))

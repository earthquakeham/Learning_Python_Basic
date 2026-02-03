# Step4. Step by step optimize!

# ① 판단이 필요한 부분은 없는가?
#   예제는 별도의 판단문을 추가 할 필요가 없음

# ② 반복 되는 것은 없는가?
#   비슷한 계산이 8번 반복된다.

# input = 2
# results = []
# for number in range(2,10):
#     result = input * number
#     results.append(result)
# print(results)

# ③ Module화(기능화) 시킬 것은 없는가?
#   계산 과정을 별도의 기능으로 만들면 어떨까?

# input = 2
# def gugu(input):
#     results = []
#     for number in range(2,10):
#         result = input * number
#         results.append(result)
#     return results
# print(gugu(input))

# ④ 간소화 시킬 부분은 없는가?
#   list 생성과 내용 추가 어떨까? 이 부분은 앞에서 반영함
#   for 문을 조금 더 간단하게 표현 할 수 있지 않을까?

# input = 2
# def gugu(input):
#     results = []
#     for number in range(2,10):
#         results.append(input * number)
#     return results
# print(gugu(input))

# ⑤ 조금 더 보완 할 부분은 없는가?
# For 가 아닌 while을 사용하는 것이 더욱 simple 하지 않을까?
# 2단 뿐만 아니라 원하는 단을 사용자에게 입력 하게 하는 것은 어떨까?

input = int(input("Input numer : "))
def gugu(input):
    results = []
    number = 2
    while number < 10:
        results.append(input * number)
        number = number + 1
    return results
print(gugu(input))


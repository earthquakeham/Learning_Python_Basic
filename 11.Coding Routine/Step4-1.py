# Step4. Step by step optimize!

# ① 판단이 필요한 부분은 없는가?
#   예제는 별도의 판단문을 추가 할 필요가 없음

# ② 반복 되는 것은 없는가?
#   비슷한 계산이 8번 반복된다.

input = 2

for number in range(2,10):
    result = input * number
    print(result)
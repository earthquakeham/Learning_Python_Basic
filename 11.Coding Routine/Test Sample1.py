# 특정한 자연수를 입력 받아서 그 안에 있는 3, 5의 배수의 합을 출력한다.

# Step1. Basic
# number = int(input("Input integer : "))
# sum = 0
# for i in range(1,number):
#     if i % 3 == 0:
#         sum = sum + i
# print(sum)

# Step2. Add... Modify...
number = int(input("Input integer : "))
sum = 0
for i in range(1,number):
    if (i % 3 == 0) or (i % 5 == 0):
        sum = sum + i
print(sum)

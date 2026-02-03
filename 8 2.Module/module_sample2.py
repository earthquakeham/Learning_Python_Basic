# if __name__ == "__main__" 있는 경우

def calculation1(a,b):
    sum = a + b
    mul = a * b
    return print("Sum : %i, Mul : %i" %(sum, mul))

def calculation2(a,b):
    if type(a) != type(b):
        return print("a and b are different type!")
    else:
        sum = a + b
        mul = a * b
        return print("Sum : %i, Mul : %i" %(sum, mul))

if __name__ == "__main__":  # 이 부분의 역할 이해
    calculation1(5,6)
    calculation2(45,90)

    
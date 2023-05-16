def exampleOne(a):
    if type(a) == int:
        return a
    else :
        print('정수를 입력해야 합니다.')

print(exampleOne(10))
print(exampleOne(0.1))
print(exampleOne(-1))
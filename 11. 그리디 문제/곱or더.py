string = input()

result = int(string[0])
# 두번째 값부터 시작
for str in string[1:]:
    num = int(str)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)

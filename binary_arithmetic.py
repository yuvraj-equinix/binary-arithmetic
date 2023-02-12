NUMBER_LENGTH = 32


def decimal_to_binary(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = num * (-1)

    bin = [0] * NUMBER_LENGTH
    for i in range(NUMBER_LENGTH - 1, -1, -1):
        bin[i] = num % 2
        num = num // 2

    if is_negative:
        bin = complement_2(bin)
    return bin


def binary_to_decimal(arr):
    is_negative = False
    if arr[0] == 1:
        is_negative = True
        arr = complement_2(arr)
    num = 0
    for i in range(1, NUMBER_LENGTH):
        num = num + arr[i] * 2 ** (31 - i)
    if is_negative:
        return -num
    return num


def complement_2(arr):
    ans = arr[:]
    for i in range(NUMBER_LENGTH):
        ans[i] = 0 if arr[i] == 1 else 1
    return add_binary(ans, decimal_to_binary(1))


def add_binary(bin1, bin2):
    ans = [0] * NUMBER_LENGTH
    carry, i = 0, NUMBER_LENGTH - 1
    while i >= 0:
        sum = bin1[i]
        sum += bin2[i]
        sum += carry

        ans[i] = sum % 2
        carry = sum // 2

        i -= 1
    return ans


def sub_binary(bin1, bin2):
    c = complement_2(bin2)
    ans = add_binary(bin1, c)
    return ans


def multiply_binary(bin1, bin2):
    is_negative = False
    decimal1 = binary_to_decimal(bin1)
    decimal2 = binary_to_decimal(bin2)

    if decimal1 < 0:
        bin1 = complement_2(bin1)
        is_negative = not is_negative
    if decimal2 < 0:
        bin2 = complement_2(bin2)
        is_negative = not is_negative

    ans = [0] * NUMBER_LENGTH
    for i in range(NUMBER_LENGTH - 1, -1, -1):
        curr_multiplication = [0] * NUMBER_LENGTH
        k = i
        for j in range(NUMBER_LENGTH - 1, -1, -1):
            if k > -1:
                curr_multiplication[k] = bin2[i] and bin1[j]
                k -= 1
        ans = add_binary(ans, curr_multiplication)

    if is_negative:
        return complement_2(ans)
    return ans


def div_binary(bin1, bin2):
    count = 0
    while binary_to_decimal(bin1) >= binary_to_decimal(bin2):
        bin1 = sub_binary(bin1, bin2)
        count += 1

    ans = decimal_to_binary(count)
    return ans


def factorial_binary(bin):
    decimal = binary_to_decimal(bin)
    ans = 1
    for i in range(1, decimal + 1):
        ans *= i

    return decimal_to_binary(ans)


def power_binary(bin1, bin2):
    decimal2 = binary_to_decimal(bin2)
    if decimal2 < 0:
        return 0
    res = decimal_to_binary(1)
    for _ in range(decimal2):
        res = multiply_binary(res, bin1)
    return res


def mod_binary(bin1, bin2):
    decimal1 = binary_to_decimal(bin1)
    decimal2 = binary_to_decimal(bin2)

    ans = decimal1 % decimal2
    return decimal_to_binary(ans)


while True:
    print("Select Operation")
    print("+ => Addition")
    print("- => Substraction")
    print("* => Multiplication")
    print("/ => Division")
    print("! => Factorial")
    print("^ => Power")
    print("% => Modulus")
    print("q => Exit")

    operator = input()
    if operator == "q":
        break
    print("Enter the First Number")
    num1 = int(input())
    bin1 = decimal_to_binary(num1)
    if operator != "!":
        print("Enter the Second Number")
        num2 = int(input())
        bin2 = decimal_to_binary(num2)

    if operator == "+":
        ans = add_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == "-":
        ans = sub_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == "*":
        ans = multiply_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == "/":
        ans = div_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == "!":
        ans = factorial_binary(bin1)
        print(binary_to_decimal(ans))
    elif operator == "^":
        ans = power_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == "%":
        ans = mod_binary(bin1, bin2)
        print(binary_to_decimal(ans))
    else:
        print("Invalid Input")

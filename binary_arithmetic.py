NUMBER_LENGTH = 32

def decimal_to_binary(num):
    bin = [0] * NUMBER_LENGTH
    for i in range(NUMBER_LENGTH - 1, -1, -1):
        bin[i] = num % 2
        num = num // 2
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
    return add(ans, decimal_to_binary(1))


def add(bin1, bin2):
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


def sub(bin1, bin2):
    c = complement_2(bin2)
    ans = add(bin1, c)
    return ans


def mul(bin1, bin2):
    is_negative = False
    a_decimal = binary_to_decimal(bin1)
    b_decimal = binary_to_decimal(bin2)

    if a_decimal < 0:
        bin1 = complement_2(bin1)
        is_negative = not is_negative
    if b_decimal < 0:
        bin2 = complement_2(bin2)
        is_negative = not is_negative

    ans = [0] * NUMBER_LENGTH
    for i in range(NUMBER_LENGTH - 1, -1, -1):
        curr_multiplication = [0]*NUMBER_LENGTH
        k = i
        for j in range(NUMBER_LENGTH - 1, -1, -1):
            if k > -1:
               curr_multiplication[k] = bin2[i] and bin1[j]
               k -= 1
        ans = add(ans, curr_multiplication)

    if is_negative:
        return complement_2(ans)
    return ans


def div(bin1, bin2):
    pass


while True:
    print("Enter the First Number")
    num1 = int(input())
    bin1 = decimal_to_binary(num1)
    print("Enter the Second Number")
    num2 = int(input())
    bin2 = decimal_to_binary(num2)
    print("Enter the Operator")
    operator = input()

    if operator == '+':
        ans = add(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == '-':
        ans = sub(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == '*':
        ans = mul(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == '/':
        ans = div(bin1, bin2)
        print(binary_to_decimal(ans))
    else:
        print("Invalid Input")
    

# import colorama
# from colorama import Fore

NUMBER_LENGTH = 32

def decimal_to_binary(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = num*(-1)

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
    return Addition(ans, decimal_to_binary(1))


def Addition(bin1, bin2):
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


def Substraction(bin1, bin2):
    c = complement_2(bin2)
    ans = Addition(bin1, c)
    return ans


def Multiplication(bin1, bin2):
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
        ans = Addition(ans, curr_multiplication)

    if is_negative:
        return complement_2(ans)
    return ans


def Division(bin1, bin2):
    count = 0
    while binary_to_decimal(bin1) >= binary_to_decimal(bin2):
        bin1 = Substraction(bin1, bin2)
        count += 1
    
    ans = decimal_to_binary(count)
    return ans

def factorial(bin):
    number = binary_to_decimal(bin)
    ans = 1
    for i in range(1, number + 1):
        ans *= i
    
    return decimal_to_binary(ans)

def Power(bin1, bin2):
    pass

def Modulus(bin1, bin2):
    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)

    ans = num1 % num2
    return decimal_to_binary(ans)

while True:
    print("Select Operation")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Power")
    print("7. Modulus")
    print("8. Exit")

    operator = int(input())
    if operator == 8:
        break
    print("Enter the First Number")
    num1 = int(input())
    bin1 = decimal_to_binary(num1)
    if operator != 5:
       print("Enter the Second Number")
       num2 = int(input())
       bin2 = decimal_to_binary(num2)

    if operator == 1:
        ans = Addition(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == 2:
        ans = Substraction(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == 3:
        ans = Multiplication(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == 4:
        ans = Division(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == 5:
        ans = factorial(bin1)
        print(binary_to_decimal(ans))
    elif operator == 6:
        ans = Power(bin1, bin2)
        print(binary_to_decimal(ans))
    elif operator == 7:
        ans = Modulus(bin1, bin2)
        print(binary_to_decimal(ans))
    else:
        print("Invalid Input")
    

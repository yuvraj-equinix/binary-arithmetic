def decimal_to_binary(num):
    bin = [0] * 32
    for i in range(31, -1, -1):
        bin[i] = num % 2
        num = num // 2
    return bin


def binary_to_decimal(arr):
    is_negative = False
    if arr[0] == 1:
        is_negative = True
        arr = complement_2(arr)
    num = 0
    for i in range(1, 32):
        num = num + arr[i] * 2 ** (31 - i)
    if is_negative:
        return -num
    return num


def complement_2(arr):
    ans = arr[:]
    for i in range(32):
        ans[i] = 0 if arr[i] == 1 else 1
    return add(ans, decimal_to_binary(1))


def add(a, b):
    ans = [0] * 32
    carry, i = 0, 31
    while i >= 0:
        sum = a[i]
        sum += b[i]
        sum += carry

        ans[i] = sum % 2
        carry = sum // 2

        i -= 1
    return ans


def sub(a, b):
    c = complement_2(b)
    ans = add(a, c)
    return ans


def mul(a, b):
    is_negative = False
    a_decimal = binary_to_decimal(a)
    b_decimal = binary_to_decimal(b)
    if a_decimal < 0 and b_decimal > 0 or b_decimal < 0 and a_decimal > 0:
        is_negative = True
    ans = [0] * 32
    for i in range(abs(b_decimal)):
        ans = add(ans, a)
    if is_negative:
        return complement_2(ans)
    return ans


def div(a, b):
    pass


a = decimal_to_binary(3)
b = decimal_to_binary(-5)
ans = mul(a, b)
print(ans)
print(binary_to_decimal(ans))

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


def add(bin1, bin2):
    ans = [0] * 32
    carry, i = 0, 31
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
    if a_decimal < 0 and b_decimal > 0 or b_decimal < 0 and a_decimal > 0:
        is_negative = True
    ans = [0] * 32
    for i in range(abs(b_decimal)):
        ans = add(ans, bin1)
    if is_negative:
        return complement_2(ans)
    return ans


def div(bin1, bin2):
    pass


a = decimal_to_binary(3)
b = decimal_to_binary(-5)
ans = mul(a, b)
print(ans)
print(binary_to_decimal(ans))

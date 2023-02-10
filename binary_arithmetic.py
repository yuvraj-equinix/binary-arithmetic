def decimal_to_binary(num):
    bin = [0] * 32
    for i in range(31, -1, -1):
        bin[i] = num % 2
        num = num // 2
    return bin
    
def binary_to_decimal(arr):
    num = 0
    for i in range(32):
        num = num + arr[i] * 2**(31-i)
    return num

def complement_2(arr):
    ans = arr[:]
    for i in range(32):
        ans[i] = 0 if arr[i] == 1 else 1
    return add(ans, decimal_to_binary(1))

def add(a, b):
    ans = [0]*32
    carry, i = 0, 31
    while i >= 0:
        sum = a[i]
        sum += b[i]
        sum += carry
        
        ans[i] = sum%2
        carry = sum//2
    
        i -= 1
    return ans
    
def sub(a, b):
    c = complement_2(b)
    ans = add(a, c)
    return ans
    
def mul(a, b):
    pass
    
def div(a, b):
    pass
    


a = decimal_to_binary(-6)
b = decimal_to_binary(-4)
ans = sub(a, b)
print(ans)

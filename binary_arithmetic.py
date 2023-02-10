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
    return Binary(binary_to_decimal(ans), 1).add()

class Binary:
    def __init__(self, a, b):
        self.a = decimal_to_binary(a)
        self.b = decimal_to_binary(b)
        self.a_decimal = a
        self.b_decimal = b
    
    def add(self):
        pass
        
    def sub(self):
        pass
        
    def mul(self):
        pass
        
    def div(self):
        pass
        


ans = decimal_to_binary(7)
ans2 = binary_to_decimal(ans)
ans3 = complement_2(ans)
print(ans)
print(ans2)
print(ans3)

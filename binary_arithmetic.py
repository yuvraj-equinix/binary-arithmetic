def decimal_to_binary(num):
    bin = [0] * 32
    for i in range(31, -1, -1):
        bin[i] = num % 2
        num = num // 2
    return bin
    
def binary_to_decimal(self, arr):
    pass

def complement_2(arr):
    pass

class Binary:
    def __init__(self, a, b):
        self.a = decimal_to_binary(a)
        self.b = decimal_to_binary(b)
    
    def add(self):
        pass
        
    def sub(self):
        pass
        
    def mul(self):
        pass
        
    def div(self):
        pass
        


ans = decimal_to_binary(5)
print(ans)

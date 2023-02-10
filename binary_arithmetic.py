class Binary:
    def __init__(self, a, b):
        self.a = decimal_to_binary(a)
        self.b = decimal_to_binary(b)
    
    def add(self, a, b):
        ans = [0]*32
        carry, i, j = 0, 31, 31
        while i >= 0 and j >= 0:
            sum = a[i]
            sum += b[i]
            sum += carry
            
            ans[i] = sum%2
            carry = sum//2
        
            i -= 1
            j -= 1
        decimal_to_binary(ans)
        
    def sub(self, a, b):
        ans = [0]*32
        
        
    def mul(self, a, b):
        pass
        
    def div(self, a, b):
        pass
        
    def decimal_to_binary(self, num):
        bin_a = [0] * 32
        bin_b = [0] * 32
        for i in range(31, -1, -1):
            bin_a[i] = num % 2
            # todo
        
    def binary_to_decimal(self, arr):
        pass

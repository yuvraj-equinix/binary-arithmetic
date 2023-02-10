class Binary:
    def __init__(self, a, b):
        self.a = decimal_to_binary(a)
        self.b = decimal_to_binary(b)
    
    def add(self, a, b):
        pass
        
    def sub(self, a, b):
        pass
        
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

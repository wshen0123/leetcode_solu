class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        L_a = len(a)
        L_b = len(b)
        carry = 0
        result = 
        
        if L_a > L_b:
            b = "0" * (L_a - L_b) + b
        else:
            a = "0" * (L_b - L_a) + a
        
        for i in range(max(L_a, L_b), -1, -1):
            
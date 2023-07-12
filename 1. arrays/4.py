def plusOne(digits):
    n = len(digits)
    carry = 1  
    
    for i in range(n - 1, -1, -1):  
        digits[i] += carry  
        carry = digits[i] // 10  
        
        if carry == 0:
            break  
        
        digits[i] %= 10  
        
    if carry > 0:
        digits.insert(0, carry)  
        
    return digits


digits = [1, 2, 3]
result = plusOne(digits)
print(result)

# Prime factors program:

#Here's a simple Python program:
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors[::-1]

# Example usage
number = 36
print(f"Prime factors of {number} in descending order: {prime_factors(number)}")
#Binary to decimal conversion program:
def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** i)
    return decimal

# Example usage
binary_numbers = ["11000101", "10101010", "11111111", "10000000", "1111100000"]
for binary in binary_numbers:
    print(f"Binary: {binary} -> Decimal: {binary_to_decimal(binary)}")
    
#Decimal to binary conversion program:
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Example usage
decimal_numbers = [10, 27, 128, 255, 63]
for decimal in decimal_numbers:
    print(f"Decimal: {decimal} -> Binary: {decimal_to_binary(decimal)}")
class InfixToPostfixConverter:
    def __init__(self):
        self.infix = ""
        self.postfix = ""

    def get_infix(self, expression):
        self.infix = expression

    def show_infix(self):
        return f"Infix Expression: {self.infix}"

    def show_postfix(self):
        return f"Postfix Expression: {self.postfix}"

    def precedence(self, op):
        if op in {'+', '-'}:
            return 1
        elif op in {'*', '/'}:
            return 2
        return 0

    def convert_to_postfix(self):
        stack = []
        for sym in self.infix:
            if sym.isalnum():
                self.postfix += sym
            elif sym == '(':
                stack.append(sym)
            elif sym == ')':
                while stack and stack[-1] != '(':
                    self.postfix += stack.pop()
                stack.pop()  # Discard '('
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(sym):
                    self.postfix += stack.pop()
                stack.append(sym)
        while stack:
            self.postfix += stack.pop()

# Example usage
expressions = ["A + B - C", "(A + B) * C", "(A + B) * (C - D)", "A + ((B + C) * (E - F) - G) / (H - I)", "A + B * (C + D) - E / F * G + H"]
for expr in expressions:
    converter = InfixToPostfixConverter()
    converter.get_infix(expr)
    converter.convert_to_postfix()
    print(converter.show_infix())
    print(converter.show_postfix())

'''# ¼öÁ¤º»
decimal_number = (int)(input())
octal_number = oct(decimal_number)
hexadecimal_number = hex(decimal_number)
print(octal_number[2:] + ' ' + hexadecimal_number.upper()[2:])'''


a = (int)(input())
o = format(a, 'o')
h = format(a, 'x').upper()
print(o + ' '+ h)



# 74
# 3c28
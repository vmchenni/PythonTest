# Write a program for String Formatting Operator %, which should include the following conversions:
# a.Character
# b.Signed decimal integer
# c.Octal integer
# d.Hexadecimal integer (UPPERcase letters)
# e.Floating point real number
# f.Exponential notation (with lowercase 'e')

# a.Character
mychar = 'A'
print("Hello %s" % mychar)

# b.Signed decimal integer
mydecimalnumber = 10.2
print("My decimal number is  %f" % mydecimalnumber)

# c.Octal integer
myOctalNumberis = 0X7AE
print("My octal number is %o" % myOctalNumberis)

# d.Hexadecimal integer (UPPERcase letters)
myHexaDecimalNumber = 0xDA5
print("My Hexadecimal number is %X" % myHexaDecimalNumber)

# e.Floating point real number
myFloatingPointNumber = -2345.6789
print("My floating point number is %f" % myFloatingPointNumber)

# f.Exponential notation (with lowercase 'e')
myExpNumber = -3.14e-2
print("My exponential  number is %e" % myExpNumber)
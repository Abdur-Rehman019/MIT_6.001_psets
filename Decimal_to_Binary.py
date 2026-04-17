#floating point decimal to binary representation.

num = 10.01

integer = int(num)
decimal = num - integer


#splitted the integers and the decimals
#convert to binary the integer one .
bin_res = ''
integer = int(integer)
while (integer) > 0:
    bin_res = str(integer%2) + bin_res
    integer = integer//2
#integer part sorted

#decimal part
dec_res =''
precision = 10

while decimal > 0 and precision > 0:
    decimal *= 2
    bit = int(decimal)  # 0 or 1
    dec_res += str(bit)
    decimal -= bit      # keep fractional part
    precision -= 1

# final result
print(bin_res + "." + dec_res)

    



    

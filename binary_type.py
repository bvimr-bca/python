#binary data type program
b = bytes([10,20,30,40])
print(type(b))
print(b)


#accessing elements
print(b[0])
print(b[1])

for byte in b:
    print(byte, end =' ')


#bytearray example
ba = bytearray([202,30,40])
print(ba)

#modification
ba[2] = 99
print(ba)

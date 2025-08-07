from Signature.signature import sign
print("Byte Example")

#creating Byte object

b = bytes([65,66,67,68])
print(b)
#accessing elements in byte objects
print(b[0])
print(b[1])

#using loop to iterate
for byte in b:
    print(byte,end=' ')

print("\n")
#Bytearray
ba = bytearray([65,66,67,68])
print(ba)

#Changing elements
print("Looping through byte array \n\n")
ba[0] = 97
for byte in ba:
    print(byte,end=' ')
#Adding elements
ba.append(1)
print(ba)

#converting byte array to byte
print("Converting byte array into byte")
b_converted = bytes(ba)
print(b_converted)

#memory view example
print("memory view")
b_mv = bytes([65,66,67,68,69])

mv = memoryview(b_mv)
print(mv)


#Slicing mv
print("Slicing memory view")
mv_slice = mv[1:4]
print(mv_slice)

#creatinv byte array of memory  view
print("CReating byte array of memory view")
ba_mv = bytearray([65,66,67,68,69])
mv_ba = memoryview(ba_mv)
print(mv_ba)
print("Value of mv_ba 0 index")
print(mv_ba[0])

#modifying the original byte array throught memory view
print("modifying the ba_mv element")
mv_ba[0] = 97
print(ba_mv)
# trying =bytes("Helloo",'utf-8')
# print(trying)
print()



print("\n")
print("\n")
sign("Yash","015")
from Signature.signature import sign
print("Showcasing multiple ways to swap two varaiables as follow")
a = 5
b = 10
print(f"Here A :{a} B: {b} originally")
print("Swapping using temporary varieable")
temp = b
b = a
a = temp
print(f"After swapping A :{a} B: {b}")



a = 5
b = 10

#Swapping using mathematical operation
a = a+b
b = a-b
a = a-b
print(f"After swapping A :{a} B: {b}")

#Swapping using a,b = b,a 
a = 5
b = 10
a,b = b,a
print(f"After swapping A :{a} B: {b}")
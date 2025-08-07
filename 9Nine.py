from Signature.signature import sign
#Program to demonstrate core objets and function
print("Demostrating core objects and function")

#input is an object used to take input in string which can be type casted using int()

num_list = input("Please enter number list")

user_input = num_list.split(' ')

#Converting it into integer
numbers = list(map(int,user_input))

total = sum(numbers)

length = len(numbers)

sorted_num = sorted(numbers)


#Printing
print("Displaying the outputs of above operations")
print("\nThis is the list that you have entered ", num_list,"\n")
print("This is the sum of the numbers that you have entered: ",total)
print("This is the total length of the list: ",length)
print("Here is the sorted list: ",sorted_num)

sign("Yash Sehgal","015")
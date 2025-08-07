from Signature.signature import sign
print("SHowing the datatypes")

num_type = 12   #Integer datatype
text_type = 'Hello, World!' #String type datatype
float_type = 3.14   #Float type datatype
multinum_type = [1,2,3,4,5] #List type
coords_type = (10.0,20.0)   #Tuple type datatype
subjectmarks_type = {"maths":90,
                     "English":99}  #Dictionary type data type
bool_type = True #Boolean type datatype

def identifyDtypes(): # This function prints the type of variables above
    print(type(num_type))
    print(type(text_type))
    print(type(float_type))
    print(type(multinum_type))
    print(type(coords_type))
    print(type(subjectmarks_type))
    print(type(bool_type))

identifyDtypes()
sign("Yash", "015")
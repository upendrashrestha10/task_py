#WAP to perform Arithmatic operation
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: ")) 

def addition(num1,num2):
    x=num1+num2
    return x
print("Addition: ",addition(num1,num2))

def mux(num1,num2):
    x=num1*num2
    return x
print("multiplexon: ",mux(num1,num2))

def sub(num1,num2):
    x=num1-num2
    return x
x=sub(num1,num2)
print("Subtraction: ",x)

def div(num1,num2):
    x=num1/num2
    return x
x=div(num1,num2)
print("Division: ",x)

#ALSO,
# num1=int(input("enter 1st number: "))
# num2=int(input("enter 2nd number: ")) 
# def arithmatic_operation(num1,num2):
#     print("Addition: ",num1+num2)
#     print("Subtarction: ",num1-num2)
#     print("Multiplex: ",num1*num2)
#     print("Divsion: ",num1/num2)
#     print("Modulo: ",num1%num2)
# arithmatic_operation(num1,num2)
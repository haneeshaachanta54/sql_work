#input function errors
a=input("Enter a number: ")
b=input("Enter another number: ")
print(a+b) #forgetting to convert input to integer
age=int(input("Enter age:")) #input:abc -> ValueError:invalid literal for int()
price = float(input("Enter price: "))#input:hello -> ValueError
#Output Function (print) Errors
print(Hello) #NameError: name 'Hello' is not defined
print("Python"#SyntaxError
age=20
print("Age is"+age) #TypeError
num=input("Enter number: ")
print(num * 2) 
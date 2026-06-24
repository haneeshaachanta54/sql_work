#positive number or not
n=int(input("Enter a number: "))
if n>0:
    print("Positive")
elif n==0:
    print("Zero")
else:
    print("Negative")
#2. Check whether a character is uppercase or lowercase (without using built-in functions)
ch=input("Enter a character: ")
if 'A'<=ch<='Z':
    print("Uppercase")
elif 'a'<=ch<= 'z':
    print("Lowercase")
else:
    print("Not an alphabet")
#pass or fail
s1=int(input("Enter Subject 1 marks: "))
s2=int(input("Enter Subject 2 marks: "))
s3=int(input("Enter Subject 3 marks: "))
s4=int(input("Enter Subject 4 marks: "))
s5=int(input("Enter Subject 5 marks: "))
s6=int(input("Enter Subject 6 marks: "))
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    print("PASS")
else:
    print("FAIL")
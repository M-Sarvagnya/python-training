'''try:
    a = input("Enter a value: ")
    b = int(input("Enter b value: "))
    c = float(input("Enter c value: "))
except:
    print("In-correct sequence")
else:
    print("correct sequence")'''   

'''try:
    a = input("Enter a value: ")
except:
    print("In-correct a sequence")
else:
    print("correct a sequence")
try:
    b = int(input("Enter b value: "))
except:
    print("In-correct sequence")
else:
    print("correct sequence") 
try:
    c = float(input("Enter c value: "))
except:
    print("In-correct sequence")
else:
    print("correct sequence")'''

try:
    a = input("Enter a value: ")
    b = int(input("Enter b value: "))
    c = float(input("Enter c value: "))
except ValueError:
    concat =  a + ' In-correct sequence ' + b + 'In-correct sequence' + c

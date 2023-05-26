try:
    a = input("Enter a value: ")
    b = int(input("Enter b value: "))
    c = float(input("Enter c value: "))
except ValueError:
    concat =  a + ' In-correct sequence ' + b + 'In-correct sequence' + c

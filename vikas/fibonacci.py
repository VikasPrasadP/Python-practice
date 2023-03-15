n = int(input("Enter number of terms:"))
a,b = 0,1
if n <= 0:
    print("Enter a positive value ")
elif n==1:
    print("Fibonacci series is: ")
    print(a)
else:
    print("Fibonacci series is: ")
    print(a)
    print(b)
    count=2
    while count < n:
        count = count+1
        c = a+b
        print(c)
        a,b = b,c
# Create a function for factorial
def factorial(n):
    # Return the factorial of n
    kq=1
    for i in range(1, n+1): 
      kq*=i
    return kq
      

# Read input and print result
num = int(input())
print(str(num) + "! = " + str(factorial(num)))
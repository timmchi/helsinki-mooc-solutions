# Write your solution here
numba = int(input("Number: "))

if numba % 3 == 0 and numba % 5 == 0:
    print("FizzBuzz")
elif numba % 3 == 0:
    print("Fizz")
elif numba % 5 == 0:
    print("Buzz")
else:
    pass
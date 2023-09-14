# For all integers from -30 to 30:
# ✓ if it’s a multiple of 3, display “Fizz”
# ✓ if it’s a multiple of 5, display “Buzz”
# ✓ if it’s a multiple of 3 and 5, display “FizzBuzz”
# ✓ if it does not meet any of the previous conditions, just print the integer itself.

for cnt in range(-30, 31):
    if (cnt % 3 and cnt % 5):
        print("fizzbuzz")
    elif (cnt % 3):
        print("Fizz")
    elif (cnt % 5):
        print("Buzz")
    else:
        print("rien")
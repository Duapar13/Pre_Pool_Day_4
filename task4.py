num = int(input("Enter an integer: "))
if num == 42 or num <= 21 or num % 2 == 0 or (num / 2) < 21:
    print("OK")
elif num % 2 != 0 and num >= 45:
    print("OK")
else:
    print("You got it wrong, my poor friend!")

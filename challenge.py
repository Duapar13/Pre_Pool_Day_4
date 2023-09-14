while True:
    integer = int(input("Enter an integer (0 to quit): "))
    if integer == 0:
        break
    string = input("Enter a string: ")
    if any(char in 'aeiouAEIOU' for char in string):
        print(integer)
    elif integer >= 42:
        print(integer)
    else:
        print(string)
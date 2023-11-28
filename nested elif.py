height = int(input("What's your height? "))
age = int(input("What's your age? "))

if height>=120:
    print("You can ride rollarcoaster")
    if age<=12:
        print("Pay 5")
    elif age<=15:
        print("Pay 7")
    else:
        print("Pay 12")
else:
    print("Sorry, you need to grow your height before going to rollarcoaster ride")

class Lesson3:
    # Control Flow & Functions
    # slide 4 level 1
    @staticmethod
    def ex1():
        # A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
        # Ask user for their salary and year of service and print the net bonus amount.
        salary = int(input("please enter your salary: "))
        service = int(input("please enter your year of service: "))
        if service > 5:
            print(f"bonus: {salary * 0.05}")
        else:
            print("no bonus :(")

    @staticmethod
    def ex2():
        # Take values of length and breadth of a rectangle from user and check if it is square or not.
        length = input("Enter length")
        breadth = input("Enter breadth")
        if length == breadth:
            print("Yes, it is square")
        else:
            print("No, it is only Rectangle")

    @staticmethod
    def ex3():
        # Take two int values from user and print greatest among them.
        first = int(input("Enter first number"))
        second = int(input("Enter second number"))
        if first > second:
            print(f"Greatest is {first}")
        elif second > first:
            print(f"Greatest is{second}")
        else:
            print("Both are equal")

    @staticmethod
    def ex4():
        # A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
        # Ask user for quantity
        # Suppose, one unit will cost 100.
        # Judge and print total cost for user.
        quantity = int(input("Enter quantity"))
        if quantity * 100 > 1000:
            price = (quantity * 100) * 0.9
            print(f"Cost is {price}")
        else:
            print(f"Cost is{quantity * 100}")

print("Welcome to the Trip Cost Calculator!")
day = int(input("How many days will you stay? "))
hotel = float(input("How much does hotel cost per night? $"))
flight = float(input("How much does flight cost? $"))
rental = float(input("If you need rental car please enter the price otherwise enter zero. $"))
others = float(input("Enter other possible expenses $"))

total = (day*hotel) + flight + (day*rental) + others

print(f"Total Cost: ${total}")
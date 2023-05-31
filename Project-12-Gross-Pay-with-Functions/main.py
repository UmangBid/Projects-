def compute_pay(hour, rate):
    if hour < 40:
        pay = round(hour * rate, 2)
    else:
        overtime = hour - 40
        pay = (rate * 40.0) + (rate * 1.5 * overtime)
        return pay


def check_for_float(input):
    try:
        val = float(input)
        return val
    except:
        print("Error , please enter numeric input")
        quit()


hour = input("Enter Hours:")
hour = check_for_float(hour)
rate = input("Enter rate:")
rate = check_for_float(rate)

print(compute_pay(hour, rate))

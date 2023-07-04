choice = float(input("Enter 1 for hours, 2 for minutes, 3 for seconds: "))


# Converting seconds into hours, minutes and remaining seconds
def time_convertor(seconds0):
    hours = seconds0 // 3600
    minutes = (seconds0 - hours * 3600) // 60
    remaining_seconds = (seconds0 - (minutes * 60) - (hours * 3600))
    return hours, minutes, remaining_seconds


# Converting given Minutes into hours, minutes and seconds
def time_convertor1(minutes0):
    second1 = minutes0 * 60
    hours1 = second1 // 3600
    minutes1 = (second1 - hours1 * 3600) // 60
    seconds1 = (second1 - (minutes1 * 60) - (hours1 * 3600))
    return hours1, minutes1, seconds1


# Calculating Minutes, Seconds in given hours
def time_convertor2(hours0):
    hours2 = hours0
    minutes2 = hours0 * 60
    seconds2 = hours0 * 3600
    return hours2, minutes2, seconds2


if choice == 1:
    ihour = float(input("Enter Hours: "))
    hours2, minutes2, seconds2 = time_convertor2(ihour)
    print("\nHours : " + str(hours2) + " = Minutes : " + str(minutes2) + " = Seconds : " + str(seconds2))

elif choice == 2:
    iminute = float(input("Enter Minutes: "))
    hours1, minutes1, seconds1 = time_convertor1(iminute)
    print("\nHours : " + str(hours1) + " = Minutes : " + str(minutes1) + " = Seconds : " + str(seconds1))

elif choice == 3:
    isecond = float(input("Enter Seconds: "))
    hours, minutes, remaining_seconds = time_convertor(isecond)
    print("Hours : " + str(hours) + " = Minutes : " + str(minutes) + " = Seconds : " + str(remaining_seconds))

else:
    print("Invalid Choice")

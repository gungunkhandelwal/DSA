def whichWeekDay(day):
    # Using match like switch
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid")


day=int(input())
whichWeekDay(day)

# List way

weekday=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
if 1<=day<=7:
    print(weekday[day-1])
else:
    print("Invalid")

# Dictionary way
weekdays={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(weekdays.get(day,"Invalid"))


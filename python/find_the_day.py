def day_no(no):
    switch = {
        1: 'Sunday' ,
        2: 'Monday' ,
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return switch.get(no , 'Invalid input')
s = int(input("Enter the number: "))
print("The Day is",day_no(s))
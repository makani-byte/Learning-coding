import calendar

yy = 2023
mm = int(input("Enter the month (1-12): "))

print(calendar.month(yy, mm))


day = int(input("Enter the day of the month: "))
note = input("Enter a note: ")

# Add the note to the calendar
calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthcalendar(yy, mm)
week_num = (day - 1) // 7
day_num = (day - 1) % 7
cal[week_num][day_num] = f"**{note}**"  # Highlight the note with **

# Print the updated calendar
print(calendar.month(yy, mm))
# Output the month, day, and note
print(f"Month: {calendar.month_name[mm]}, Day: {day}, Note: {note}")

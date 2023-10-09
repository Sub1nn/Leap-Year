print("Check if the year is a leap year")
year = int(input("Tell the year!\n"))

if (year % 4 == 0 & year % 100 != 0) | (year % 400 == 0):
  print("Leap year")
else:
  print("Not leap year")

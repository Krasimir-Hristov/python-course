user_number = int(input("Enter a number:"))

start = 1
stop = 11

for number in range(start, stop):
  sum = user_number * number
  print(f"{user_number} x {number} = {sum}")

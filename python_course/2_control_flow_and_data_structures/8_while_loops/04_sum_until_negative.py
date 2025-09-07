

sum_off_all_number = 0

while True:
  user_input = int(input("Enter a positive number (or a negative to exit):").strip())

  if user_input < 0:
    break

  else:
    sum_off_all_number += user_input


print(f"The sum of all positive numbers is: {sum_off_all_number}")



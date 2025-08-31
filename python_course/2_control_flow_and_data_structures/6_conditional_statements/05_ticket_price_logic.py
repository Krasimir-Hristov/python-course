age = int(input("Enter your age:"))

ticket_price = 0

if age < 12:
  ticket_price = 5
  print(f"Ticket price:{ticket_price}")

elif age >= 12 and age <= 18:
  ticket_price = 8
  print(f"Ticket price:{ticket_price}")
  
else:
  ticket_price = 12
  print(f"Ticket price:{ticket_price}")

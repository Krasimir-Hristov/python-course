allowed_users = {"krasimir", "ivan", "petar"}

username = input("Enter your username:").lower().strip()

if username in allowed_users:
  print("Access granted")

else:
  print("Access denied")  

password_accepted_lenght = 8

while True:
  user_password = input("Enter a password (min. 8 chars):").strip()

  if len(user_password) < password_accepted_lenght:
    print("Password is too short. Try again.")
    continue
  else:
    print("Password accepted")
    break

  

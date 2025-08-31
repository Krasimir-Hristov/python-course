correct_password = "python123"

user_password = input("Enter password:").strip()
print(user_password)
if correct_password == user_password:
  print("Login successful!")

else:
  print("Incorrect password.")  
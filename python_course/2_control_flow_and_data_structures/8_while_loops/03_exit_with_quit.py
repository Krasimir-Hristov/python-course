word = True

while word:
  user_input = input("Enter a message (or 'quit' to exit):")

  if user_input != 'quit':
    print(f"You said: {user_input}")
    continue

  else:
    break

print("Goodbye!")
  

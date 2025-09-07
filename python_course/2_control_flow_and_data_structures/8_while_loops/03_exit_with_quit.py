while True:
    user_input = input("Enter a message (or 'quit' to exit):")
    if user_input == 'quit':
        break # Просто излизаме
    print(f"You said: {user_input}")

print("Goodbye!")
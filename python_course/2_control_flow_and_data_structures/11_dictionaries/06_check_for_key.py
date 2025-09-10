user_permissions = {"admin": True, "editor": False}
check_role = input("Enter role to check:").lower().strip()

if check_role in user_permissions: # Това е всичко!
    print(f"Role '{check_role}' exists.")
else:
    print(f"Role '{check_role}' does not exist.")
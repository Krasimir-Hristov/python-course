user_premissions = {
  "admin" : True,
  "editor" : False
}

check_role = input("Enter role to check:").lower().strip()

roles = user_premissions.items()

for role in roles:
 
 if role[0] == check_role and role[1]:
  print(f"Role {check_role} exist.")
  break
 else:
  print(f"Role {check_role} does not exist.")
  break
  

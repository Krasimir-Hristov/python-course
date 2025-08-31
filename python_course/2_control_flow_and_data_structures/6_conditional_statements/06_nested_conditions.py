"""
I will resolve this problem using boolean flag, and very detail for training purposses.
The program will print "Acces" or "Access denied." no matter what.
"""

access = False

user_login_input = input("Are you logged in (yes/no)?").strip()

if user_login_input != "yes" and user_login_input != "no":
  print('Please restart your program and answer only with "yes" or "no"')

elif user_login_input == "no":
  print("Please restart your program, and first login.")

else:
  user_admin_input = input("Are you an admin (yes/no)?").strip()
  
  if user_admin_input != "yes" and user_admin_input != "no":
   print('Please restart your program and answer only with "yes" or "no"')
  
  if  user_admin_input == "yes":
     access = True
  else:
    print("You dont have admin premissions to read this secret file!") 


if access:
  print("Access")

else:
  print("Access denied.")       

  
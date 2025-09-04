secret_number = 7


while  secret_number:
     player_number = int(input("Guess the number:"))
     
     if player_number != secret_number:
          print("Try again!")
          continue

     else:
          print("Congratulations! You guessed the number.")
          break   

import random
random_number=random.randint(0,10)
guess_count = 1
guess_limit = 3
while guess_count<=guess_limit:
   guess=int(input("Guess a number"))
   if guess == random_number:
      print("Correct!")
      break
   else:
      if guess_count>guess_limit:
         print("Game Over.")
         break
      print("Try Again!")
      guess_count += 1
      
      

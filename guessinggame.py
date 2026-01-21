import random
guess=int(input("Guess a number"))
sol=random.randint(0,10)
i = 1
while i<=3:
   if guess == sol:
      print("Correct!")
      break
   else:
      print("Try Again!")
      i = i + 1
      if i>3:
         print("Game Over.")
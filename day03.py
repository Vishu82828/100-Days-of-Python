print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
totalname = name1+name2
name = totalname.lower()

t  = name.count("t")

r = name.count("r")

u  = name.count("u")

e  = name.count("e")

trueTotal = t+r+u+e
#true total complete

l = name.count("l")

o = name.count("o")

v = name.count("v")

e2 = name.count("e")

loveTotal = l+o+v+e2
#total love compleate

Slove = str(loveTotal)
Strue = str(trueTotal)
loveScore = Strue+Slove
score = int(loveScore)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50 :
  print(f"Your score is {score}, you are alright together.")
else : print(f"Your score is {score}.")
print(trueTotal)
print(loveTotal)
#  David Beckham	Victoria Beckham

#num_char = len(input())
#new_char = input("")
#print(num_char)
#print(type(num_char))
#print(round(52/97,1))
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
small = 15
if size=="S" :
  if add_pepperoni=="Y":
    small += 2
  if extra_cheese=="Y":
    small += 1
print(small)
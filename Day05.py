# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0
count = 0
for  i in student_heights:
  count += 1
  sum += i
avg = round(sum/count)
print(f"total height = {sum}")
print(f"number of students = {count}")
print(f"average height = {avg}")
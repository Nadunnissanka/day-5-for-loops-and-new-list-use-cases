# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
all_std_h = 0
num = 0

for height in student_heights:
  all_std_h = all_std_h + int(height)
  num += 1

print(f"Sum of height: {all_std_h}")
avg = all_std_h / num
print(f"Average is: {round(avg)}")
#Write your code below this row 👇

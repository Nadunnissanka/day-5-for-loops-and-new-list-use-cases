# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# 🚨 Don't change the code above 👆
highest_score = 0

for score in student_scores:
  if int(score) > int(highest_score):
    highest_score = score
print(f"Highest score is : {highest_score}")

#Write your code below this row 👇
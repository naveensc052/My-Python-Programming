student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
High_score = student_scores[0]
for x in student_scores:
    if x >= High_score:
        High_score = x
print(f"The highest score in the class is: {High_score}")
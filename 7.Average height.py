student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum = 0
for n in range(0, len(student_heights)):
    sum += student_heights[n]
average = sum/len(student_heights)
average = round(average)
print(average)
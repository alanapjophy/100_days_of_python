# Dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Empty dictionary
student_grades = {}

# Code for converting scores into grades
for key in student_scores:
  student_status = student_scores[key] 
  if student_status > 90:
    student_status = "Outstanding"
  elif student_status > 80: 
    student_status = "Exceeds Expectations"
  elif student_status > 70: 
    student_status =  "Acceptable"
  else:
    student_status = "Fail"
  student_grades.update({f"{key}" : f"{student_status}"})

print(student_grades)

# Code by Udemy
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
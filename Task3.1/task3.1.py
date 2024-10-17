# Data Processing with Map, Filter, Reduce

from functools import reduce

# List of students 
students = [
   {"name" : "John", "age" : 25, "grades" : [80,70,85,95]},
   {"name" : "Maya", "age" : 20, "grades" : [90,75,80,80]},
   {"name" : "Chris", "age" : 22, "grades" : [75,55,50,40]} 
]

# Extract the name of the students using map
students_name = list(map(lambda student : student ["name"], students))
print ("List of students names : ",students_name)

# filter the passed students based on grades
passing_students = list(filter(lambda student: sum(student["grades"]) / len(student["grades"]) >= 70, students))
print ("List of students who passed : ",passing_students)

# total sum of grades of the students using reduce
print("\nTotal sum of grades for each student:")
total_grades = []
for student in students:
   total_grade = reduce(lambda x, y: x + y, student["grades"])
   total_grades.append((student["name"], total_grade))
   print(f"{student["name"]}: {total_grade}")

# highest grade among students
highest_grade = max(total_grades, key = lambda x: x[1])
print("\nHighest grade:", highest_grade )

# average
passing_threshold = 75

# chain operations
print("\n--- Chaining Operations ---")
result = [
   (student["name"], sum(student["grades"]))
   for student in students
   if sum(student["grades"]) / len(student["grades"]) > passing_threshold 
]

print ("Name and total grades of students who passed :", result )

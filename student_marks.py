student_name = "Ajay"
marks = [78, 85, 90, 88, 76]

total = sum(marks)
average = total / len(marks)

print("Student Name:", student_name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 75:
    print("Result: Passed with Good Performance")
else:
    print("Result: Needs Improvement")
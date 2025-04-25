# 2- Activity : 
# You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. 
# Each row represents a student, and each column a subject. See below:

# scores = np.array([
#     [78, 85, 90],
#     [88, 79, 92],
#     [84, 76, 88],
#     [90, 93, 94],
#     [75, 80, 70]
# ])
 
# Tasks:
# Calculate and print the average score for each student.
# Calculate and print the average score for each subject.
# Identify the student (row index) with the highest total score.
# Add 5 bonus points to the third subject for all students.

import numpy as np
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

#axis = 1 means the operation is performed along the rows
average_scores_per_student = np.mean(scores, axis=1)
print(f"Average scores per student: {average_scores_per_student}")

average_scores_per_subject = np.mean(scores, axis=0)
print(f"Average scores per subject: {average_scores_per_subject}")

total_score_per_student = np.sum(scores, axis=1)
#Index of max value in the array argmax(array_to_compute,axis=1)
#since array_to_compute is a 1D array, axis parameter is not needed
highest_total_score_student = np.argmax(total_score_per_student)
print(f"Student with the highest total score is number: {highest_total_score_student}")

#using slicing and broadcasting to add 5 bonus points to the third subject for all students
scores[:,2] = scores[:,2] + 5;
print(f"Scores after adding 5 bonus points to the third subject: {scores}")
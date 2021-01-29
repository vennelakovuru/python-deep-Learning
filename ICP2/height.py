# user input for number of students
students_Num = int(input("Enter the number of students:"))
height_in_feet_list = []
height_in_cm_list = []

# user input for each student height in feet for the given num of students
# adding it to the height_in_feet_list
for i in range(1, students_Num + 1):
    height_in_feet_list.append(float(input(f"Enter height of student {i} in feet :")))
    i = i + 1

print(f"Height of students in feet: {height_in_feet_list}")

# converting each element from height_in_feet_list to cm and adding it to the height_in_cm_list
# 1 feet = 30.48 cm
for i in range(students_Num):
    height_in_cm_list.append(round((height_in_feet_list[i] * 30.48), 2))
    i = i + 1

# printing list of heights of students in cm
print(f"Height of students in cm: {height_in_cm_list}")

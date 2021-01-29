students_Num = int(input("Enter the number of students:"))
height_in_feet_list = []
height_in_cm_list = []

for i in range(1, students_Num+1):
    height_in_feet_list.append(float(input(f"Enter height of student in feet {i} :")))
    i = i+1

print(f"Height of students in feet: {height_in_feet_list}")

for i in range(students_Num):
    height_in_cm_list.append(height_in_feet_list[i]*30.48)
    i = i+1

print(f"Height of students in cm: {height_in_cm_list}")






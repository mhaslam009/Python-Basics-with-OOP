dict_students={}
print("------------------------------------------------------------")
for i in range(1,3): #5 students will enroll
    students=input(f"Enter {i}-Student Name:")
    grade=int(input("Enter his grade :"))
    dict_students[students]=grade
print(dict_students)

#assign grade:
for i_key, i_val in dict_students.items():
    if i_val < 60:
        print(f'The student {i_key} is considered fail with {i_val} marks')
    else:
        print(f'The student {i_key} is considered pass with {i_val} marks')

print("____________________________")
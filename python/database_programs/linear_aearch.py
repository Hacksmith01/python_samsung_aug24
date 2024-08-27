def linear_search(students, search_name):
    for student_id, student_name in students.items():
        if student_name == search_name:
            return student_id
    return -1

n = int(input('Enter input size: '))

students = {}
print(f'Enter the {n} students')
for j in range(n):
    student_id = int(input("Enter the student's id: "))
    student_name = input("Enter the student name: ")
    students[student_id] = student_name

print('The input data is \n', students)

search_name = input('Enter the search name: ')

student_id = linear_search(students, search_name)
if student_id == -1:
    print(f'{search_name} was not found in the list')
else:
    print(f'{search_name} was found with id {student_id}')

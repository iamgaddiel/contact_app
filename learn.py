student = {'name': 'Gaddiel', 'age': 2}

# print(student)
# print(student.get('grand_mothers_name', 'You entered an invalid dictionary key'))

print(student.get('grand_mothers_name', None))
# print(student['class'])


# try:
#     print(student['class'])
# except KeyError:
#     print('You entered an invalid dictionary key')
from unicodedata import name


student = {'name':'John','age':'25','course':['Math','Science']}
#print(student['name'])
#student['phone'] = '555-555'
#student['name'] = 'Jane' It will basically update .
#print(student.get('phone','Not Found'))

student.update({'name':'Jane','age':'26','phone':'555-555'})
age = student.pop('age')
print(student)
print(age)
print(len(student))
print(student.items())

#del student['age']

#for key in student.items():
     # print(key,values)



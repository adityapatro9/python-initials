emp_details = {'name': 'Aditya Patro', 'age': 29, 'location': 'Pune',
               'contact': {'personal': '9040300382', 'secondary': '8261042910'},
               'stocks': ['HDFC', 'ICICI', 'Relaxo', 'Pidilite', 'BajajFiserv']}

print(emp_details.get('name').upper())
print(emp_details['age'])
print('Personal Contact : ', emp_details.get('contact').get('personal'))
print('Secondary Contact : ', emp_details['contact']['secondary'])
print(emp_details['stocks'][1])

emp_details['industry'] = 'IT'
print(emp_details)

print(emp_details.keys())
print(emp_details.items())

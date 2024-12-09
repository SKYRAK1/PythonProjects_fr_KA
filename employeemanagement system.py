# An employee managment system to record employee names, departemnt, salary, and shift to display, update, delete, filter

db={1001:{'Name':'Soumik','Department':'R&D','Salary':50000,'Shift':'Day'}}
print('-'*152)
print(f'{' '*60}Beyond Stars Dynamics')
print('-'*152)
while True:
    print('''
        1.Add Employee Details
        2.Display Employee Details
        3.Update Employee Details
        4.Delete Employee Details
        5.Statistics
        6.Filter
        ''')
    
    ch=int(input("Enter your choice: "))

    if ch == 1:
        Id = max(db.keys()) + 1 if db else 1
        name=input('Enter the name: ')
        department=input('Enter the department: ')
        salary=float(input('Enter the salary: '))
        shift=input('Enter shift: ')
        db[Id]={'Name':name,'Department':department,'Salary':salary,'Shift':shift}
        print('Information added successfully...!!!')

    elif ch == 2:
        print('-'*146)
        print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format('Id','Name','Department','Salary','shift'))
        print('-'*146)
        for Id in db:
            print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format(Id,db[Id]['Name'],db[Id]['Department'],db[Id]['Salary'],db[Id]['Shift']))
            print('-'*146)

    elif ch == 3:
        Id=int(input('Enter the Id no.: '))
        print('''
            1.Name
            2.Department
            3.Salary
            4.Shift
            ''')
        sl=int(input('Enter your selection: '))
        if sl == 1:
            un=input('Enter name: ')
            db[Id]['Name']=un
            print('Name updated successfully...!!!')

        elif sl == 2:
            ud=input('Enter department: ')
            db[Id]['Department']=ud
            print('Department updated successfully...!!!')

        elif sl == 3:
            us=float(input('Enter salary: '))
            db[Id]['Salary']=us
            print('Salary updated successfully...!!!')

        elif sl == 4:
            ush=input('Enter shift: ')
            db[Id]['Shift']=ush
            print('Shift updated successfully...!!!')

        else:
            print('Invalid Selection...!!!')

    elif ch == 4:
        Id=int(input('Enter Id no.: '))
        if Id in db:
            del db[Id]
            print('Id no. deleted successfully...!!!')
        else:
            print('Invalid ID...!!!')

    elif ch == 5:
        total_employees=len(db)
        total_salary=sum(db[Id]['Salary'] for emp in db.values())
        print('-'*146)
        print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format('Id','Name','Department','Salary','shift'))
        print('-'*146)
        for Id in db:
            print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format(Id,db[Id]['Name'],db[Id]['Department'],db[Id]['Salary'],db[Id]['Shift']))
        print('-'*146)
        print('|{:^144}|'.format(f'Total Employee: {total_employees}'))
        print('|{:^144}|'.format(f'Total Salary: {total_salary}'))
        print('-'*146)
        
    elif ch==6:
        keyword = input('Enter the keyword to filter by (e.g., department name, shift): ')
        print('-' * 146)
        print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format('Id', 'Name', 'Department', 'Salary', 'Shift'))
        print('-' * 146)
        for Id, details in db.items():
            if keyword in details['Department']or keyword in details['Shift']:
                print('|{:^28}|{:^28}|{:^28}|{:^28}|{:^28}|'.format(Id, details['Name'], details['Department'], details['Salary'], details['Shift']))
                print('-' * 146)
    else:
        print('Invalid Selection...!!!')

    s = input('Do you want to continue?(y/n): ')
    if s =='n':
        break





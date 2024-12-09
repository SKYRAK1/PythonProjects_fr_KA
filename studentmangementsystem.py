# A student management system to add, display, update, delete. search, filter. and fees installment of school students

db={1:{'name':'soumik','city':'pune','passing year':2024,'percentage':78,'course':'python','fee':17000}}
print('-'*171)
print(f'{' '*70}welcome to The kiran Academy')
print('-'*171)
while True:
    print('''
    1.Add student Details
    2.Dispaly Student Details
    3.Update
    4.Delete
    5.Search
    6.Filter
    7.Fees Installment
    ''')
    ch=int(input('Enter Your Choice: '))
    if ch==1:
        reg=max(db.keys()) + 1 if db else 1
        name=input('Enter the Name: ')
        city=input('Enter the City: ')
        passing_year=int(input('Enter the Passing Year: '))
        per=float(input('Enter the Percentage: '))
        course=input('Enter the Course: ')
        fee=eval(input('Enter the Fee: '))
        db[reg]={'name':name,'city':city,'passing year':passing_year,'percentage':per,'course':course,'fee':fee}
        print('Information Updated Successfully...!!!')
    elif ch==2:
        print('-'*149)
        print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Registration no','name','city','passing year','percentage','course','fee'))
        print('-'*149)
        for reg in db:
            print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing year'],db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
            print('-'*149)
    elif ch==3:
        reg=int(input('please provide your registration no.: '))
        print("""
        1.Name
        2.City
        3.Passing year
        4.Percentage
        5.Course
        6.fee
        """)
        sl=int(input('Enter your selection: '))
        if sl==1:
            #var[key]=uvalue
            un=input('enter name: ')
            db[reg]['name']=un
            print('name updated sucessfully...!!!')
        elif sl==2:
            uc=input('enter city: ')
            db[reg]['city']=uc
            print('city updated sucessfully...!!!')
        elif sl==3:
            upy=int(input('enter passing year: '))
            db[reg]['passing year'] = upy
            print('passing year updated sucessfully...!!!')
        elif sl==4:
            upe=float(input('enter percentage: '))
            db[reg]['percentage']=upe
            print('percentage updated sucessfully...!!!')
        elif sl==5:
            ucr=input('enter course: ')
            db[reg]['course']=ucr
            print('course updated sucessfully...!!!')
        elif sl==6:
            uf=eval(input('enter fee: '))
            db[reg]['fee']=uf
            print('fee updated sucessfully...!!!')
        else:
            print('Invalid selection...!!!')

    elif ch==4:
        reg=int(input('enter the registration no: '))
        del db[reg]
        print('Information deleted successfully...!!!')
    elif ch==5:
        reg=int(input('Enter the registration number to search: '))
        if reg in db:
            print('-'*149)
            print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Registration no','name','city','passing year','percentage','course','fee'))
            print('-'*149)
            print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing year'],db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
            print('-'*149)
        else:
            print('No record found with the given registration number.')
    elif ch==6:
        keyword = input('Enter the keyword to filter by (city, course, etc.): ')
        results = []
        print('-'*150)
        print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Registration no', 'name', 'city', 'passing year', 'percentage', 'course', 'fee'))
        print('-'*150)
        for reg, details in db.items():
            if keyword in details['city'] or keyword in details['course'] or keyword in str(details['fee']):
                results.append((reg, details))
        if results:
            for reg, details in results:
                print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(reg, details['name'], details['city'], details['passing year'], details['percentage'], details['course'], details['fee']))
                print('-'*150)
        else:
            print('No records found matching the keyword.')
    elif ch==7:
        reg=int(input('enter the registration no.: '))
        inst=float(input('enter the amount: '))
        if reg in db:
            #var[key][skey]=uvalue
            db[reg]['fee'] = inst
            print('fee detail updated successfully...!!!')
        else:
            print('Registration number not found...!!!')
    else:
        print('Invalid Input')
    c=input('Do you want to continue.(y/n): ')
    if c=='n':
        break



















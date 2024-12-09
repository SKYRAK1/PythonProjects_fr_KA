# A billing system to add, display, update, delete, and calculate items,quantity and their price.

db={1:{'Item name':'Tea','Quantity':1,'Rate':10,'Total':10}}
print('-'*152)
print(f'{' '*70}Cera Snacks Center')
print('-'*152)
while True:
    print('''
    1.Add The item
    2.Display Menu
    3.Update the Menu
    4.Delete the Bill
    5.Calculate the Items
    ''')
    ch=int(input('Enter your Choice: '))

    if ch == 1:
        bill=max(db.keys()) + 1 if db else 1
        item=input('Enter the item: ')
        Quan=int(input('Enter the quantity: '))
        price=float(input('Enter the price: '))
        total_amount=Quan*price
        db[bill]={'Item name':item,'Quantity':Quan,'Rate':price,'Total':total_amount}
        print('Item added successfully...!!!')


    elif ch == 2:
        print('-'*152)
        print('|{:^29}|{:^29}|{:^29}|{:^29}|{:^29}|'.format('Bill no.','Item','Quantity','Rate','Total'))
        print('-'*152)
        for bill in db:
            print('|{:^29}|{:^29}|{:^29}|{:^29}|{:^29}|'.format(bill,db[bill]['Item name'],db[bill]['Quantity'],db[bill]['Rate'],db[bill]['Total']))
            print('-'*152)

    elif ch == 3:
        pass #var[key]=uvalue
        bill=int(input('Enter the bill no.: '))
        print('''
            1.Item
            2.Quantity
            3.Rate
            ''')
        sl=int(input('Enter your selection: '))
        if sl == 1:
            ui=input('Enter the item name: ')
            db[bill]['Item']=ui
            print('Item Updated Successfully...!!!')

        elif sl == 2:
            uq=int(input('Enter the quantity: '))
            if uq != db[bill]['Quantity']:
                db[bill]['Rate'] *= uq / db[bill]['Quantity']
                db[bill]['Quantity']=uq
                print('quantity Updated Successfully...!!!')

        elif sl == 3:
            ur=input('Enter the rate: ')
            db[bill]['Rate']=ur
            print('Rate Updated Successfully...!!!')

        else:
            print('Invalid Selection...!!!')

    elif ch == 4:
        bill=int(input('Enter the bill no.: '))
        if bill in db:
            del db[bill]
            print('Bill no. deleted successfully...!!!')
        else:
            print('Bill not found...!!!')

    elif ch == 5:
        grand_total = sum(db[bill]['Total'] for bill in db)
        print('-' * 151)
        print('|{:^29}|{:^29}|{:^29}|{:^29}|{:^29}|'.format('Bill no.', 'Item', 'Quantity', 'Rate', 'Total'))
        print('-' * 151)
        for bill in db:
            print('|{:^29}|{:^29}|{:^29}|{:^29}|{:^29}|'.format(
                bill, db[bill]['Item name'], db[bill]['Quantity'], db[bill]['Rate'], db[bill]['Total']
            ))
        print('-' * 151)
        print(f"{' ' * 95}Grand Total: {grand_total}")
        print('-' * 151)
    else:
        print('Invalid Selection...!!!')

    s=input('Do you want to continue?(y/n): ')
    if s == 'n':
        break
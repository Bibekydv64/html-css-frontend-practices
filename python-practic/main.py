# ATM SYSTEM
# │
# ├── 1. Login
# │
# ├── 2. ATM Menu
# │   ├── Check Balance
# │   ├── Deposit Money
# │   ├── Withdraw Money
# │   └── Exit
# │
# └── 3. End Program


def login():
    username_input = input('Enter a name:')
    user_password = input('Enter a password:')

    if username_input == 'parash' and user_password == '123':
        balance = int(input('Enter a balance:'))
        home(balance)
    else:
        print('Chal bete side lag name and password galti xai bhai')


def home(balance):
    balance = balance
    user_input1 = input(
                        '''
                        1. cheak balance
                        2. deposite balance
                        3. withdrowl    
                        4. Exit
                        '''
                        )


    match user_input1:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            print('Exit program sucessfully:')
        case _:
            print('invalid input try again bete!')


    
    
login()






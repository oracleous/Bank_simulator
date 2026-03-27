'''
def myfunc(*numbers):
	number = 0
	for num in numbers:
	    if num > number:
            print(num)
        else:
            print(number) 
		number += num 
myfunc(3,6,9,3,10,89,100,688)
'''

#Simple Bank simulator 
import datetime
class Bank():
    def __init__(self):
        self.current_user = None
        self.user_base = {
        # 'Master Key': {'id': 'Internal Key', 'name': 'Name', 'balance': Amount}
        # The Action Squad
        'USER800': {'id': 'USER800', 'name': 'Al B. Back', 'balance': 5000},
        'USER801': {'id': 'USER801', 'name': 'Anna Prentice', 'balance': 150},
        'USER802': {'id': 'USER802', 'name': 'Barb Dwyer', 'balance': 3400},
        'USER803': {'id': 'USER803', 'name': 'Barry Cade', 'balance': 8900},
        'USER804': {'id': 'USER804', 'name': 'Bill Board', 'balance': 120000},
        'USER805': {'id': 'USER805', 'name': 'Brighton Early', 'balance': 750},
        'USER806': {'id': 'USER806', 'name': 'Cara Van', 'balance': 45000},
        'USER807': {'id': 'USER807', 'name': 'Chris P. Bacon', 'balance': 800},
        'USER808': {'id': 'USER808', 'name': 'Claire Voyance', 'balance': 9999},
        'USER809': {'id': 'USER809', 'name': 'Colin Allcars', 'balance': 1200},
        
        # The Botanists & Foodies
        'USER810': {'id': 'USER810', 'name': 'Corey Ander', 'balance': 300},
        'USER811': {'id': 'USER811', 'name': 'Dan D. Lion', 'balance': 50},
        'USER812': {'id': 'USER812', 'name': 'Dinah Mite', 'balance': 88888},
        'USER813': {'id': 'USER813', 'name': 'Don Ation', 'balance': 0},
        'USER814': {'id': 'USER814', 'name': 'Doug Hole', 'balance': -15}, # Overdrawn!
        'USER815': {'id': 'USER815', 'name': 'Earl E. Bird', 'balance': 600},
        'USER816': {'id': 'USER816', 'name': 'Ella Vator', 'balance': 4000},
        'USER817': {'id': 'USER817', 'name': 'Emma Rald', 'balance': 250000},
        'USER818': {'id': 'USER818', 'name': 'Faye Kaccount', 'balance': 1},
        'USER819': {'id': 'USER819', 'name': 'Frank N. Stein', 'balance': 3110},
        
        # The Dramatic Department
        'USER820': {'id': 'USER820', 'name': 'Gail Force', 'balance': 9200},
        'USER821': {'id': 'USER821', 'name': 'Gene Yuss', 'balance': 140000},
        'USER822': {'id': 'USER822', 'name': 'Gerry Mander', 'balance': 55000},
        'USER823': {'id': 'USER823', 'name': 'Gladys Saturday', 'balance': 200},
        'USER824': {'id': 'USER824', 'name': 'Hal E. Luya', 'balance': 777},
        'USER825': {'id': 'USER825', 'name': 'Harrison Fire', 'balance': 404},
        'USER826': {'id': 'USER826', 'name': 'Hazel Nutt', 'balance': 650},
        'USER827': {'id': 'USER827', 'name': 'Heidi Clare', 'balance': 3200},
        'USER828': {'id': 'USER828', 'name': 'Helen Highwater', 'balance': 900},
        'USER829': {'id': 'USER829', 'name': 'Holly Wood', 'balance': 3000000},
        
        # The Competitors
        'USER830': {'id': 'USER830', 'name': 'Homer Runn', 'balance': 40000},
        'USER831': {'id': 'USER831', 'name': 'Hugh Mungus', 'balance': 999999},
        'USER832': {'id': 'USER832', 'name': 'Ima Hogg', 'balance': 50000},
        'USER833': {'id': 'USER833', 'name': 'Ira Te', 'balance': 12},
        'USER834': {'id': 'USER834', 'name': 'Iva Problem', 'balance': 40},
        'USER835': {'id': 'USER835', 'name': 'Jack Pott', 'balance': 7777777},
        'USER836': {'id': 'USER836', 'name': 'Jay Walker', 'balance': 250},
        'USER837': {'id': 'USER837', 'name': 'Jean Poole', 'balance': 1800},
        'USER838': {'id': 'USER838', 'name': 'Jim Nastic', 'balance': 600},
        'USER839': {'id': 'USER839', 'name': 'Joe King', 'balance': 55},
        
        # The Fast & Furious
        'USER840': {'id': 'USER840', 'name': 'Joy Rider', 'balance': 80},
        'USER841': {'id': 'USER841', 'name': 'Justin Time', 'balance': 100},
        'USER842': {'id': 'USER842', 'name': 'Kara Tate', 'balance': 1500},
        'USER843': {'id': 'USER843', 'name': 'Kelly Green', 'balance': 4300},
        'USER844': {'id': 'USER844', 'name': 'Ken Tucky', 'balance': 220},
        'USER845': {'id': 'USER845', 'name': 'Kerry Oki', 'balance': 300},
        'USER846': {'id': 'USER846', 'name': 'Lee Ving', 'balance': 0},
        'USER847': {'id': 'USER847', 'name': 'Les Ismore', 'balance': 5},
        'USER848': {'id': 'USER848', 'name': 'Lois Bidder', 'balance': 10},
        'USER849': {'id': 'USER849', 'name': 'Luke Warm', 'balance': 500},
        
        # The Everyday Eccentrics
        'USER850': {'id': 'USER850', 'name': 'Lynn C. Doyle', 'balance': 120},
        'USER851': {'id': 'USER851', 'name': 'Mac Aroni', 'balance': 85},
        'USER852': {'id': 'USER852', 'name': 'Manny Kinn', 'balance': 2000},
        'USER853': {'id': 'USER853', 'name': 'Mark Mywords', 'balance': 60},
        'USER854': {'id': 'USER854', 'name': 'Marv Elous', 'balance': 50000},
        'USER855': {'id': 'USER855', 'name': 'Mary Thonn', 'balance': 262},
        'USER856': {'id': 'USER856', 'name': 'Max E. Mumm', 'balance': 999999},
        'USER857': {'id': 'USER857', 'name': 'May Day', 'balance': 911},
        'USER858': {'id': 'USER858', 'name': 'Mel O. Dramatic', 'balance': 450},
        'USER859': {'id': 'USER859', 'name': 'Mia Culpa', 'balance': 300},
        
        # The Philosophers
        'USER860': {'id': 'USER860', 'name': 'Mike Rofone', 'balance': 800},
        'USER861': {'id': 'USER861', 'name': 'Miles A. Head', 'balance': 100000},
        'USER862': {'id': 'USER862', 'name': 'Minnie Skirt', 'balance': 400},
        'USER863': {'id': 'USER863', 'name': 'Mo Mentum', 'balance': 3000},
        'USER864': {'id': 'USER864', 'name': 'Mona Lott', 'balance': 20},
        'USER865': {'id': 'USER865', 'name': 'Monty Carlo', 'balance': 85000},
        'USER866': {'id': 'USER866', 'name': 'Nat Ural', 'balance': 150},
        'USER867': {'id': 'USER867', 'name': 'Neil Down', 'balance': 10},
        'USER868': {'id': 'USER868', 'name': 'Nick O. Time', 'balance': 59},
        'USER869': {'id': 'USER869', 'name': 'Noah Lott', 'balance': 80000},
        
        # The Creative Class
        'USER870': {'id': 'USER870', 'name': 'Olive Branch', 'balance': 500},
        'USER871': {'id': 'USER871', 'name': 'Ophelia Pain', 'balance': 15},
        'USER872': {'id': 'USER872', 'name': 'Otto Matic', 'balance': 101010},
        'USER873': {'id': 'USER873', 'name': 'Paige Turner', 'balance': 350},
        'USER874': {'id': 'USER874', 'name': 'Pat Tern', 'balance': 222},
        'USER875': {'id': 'USER875', 'name': 'Paul Bearer', 'balance': 666},
        'USER876': {'id': 'USER876', 'name': 'Peg Legg', 'balance': 100},
        'USER877': {'id': 'USER877', 'name': 'Penny Weight', 'balance': 1},
        'USER878': {'id': 'USER878', 'name': 'Pete Zaria', 'balance': 1400},
        'USER879': {'id': 'USER879', 'name': 'Phil N. Blanks', 'balance': 0},
        
        # The Wildcards
        'USER880': {'id': 'USER880', 'name': 'Pierce Arrow', 'balance': 4500},
        'USER881': {'id': 'USER881', 'name': 'Polly Ester', 'balance': 1970},
        'USER882': {'id': 'USER882', 'name': 'Ray N. Bow', 'balance': 700},
        'USER883': {'id': 'USER883', 'name': 'Rex Karrs', 'balance': 50},
        'USER884': {'id': 'USER884', 'name': 'Rick O. Shay', 'balance': 300},
        'USER885': {'id': 'USER885', 'name': 'Rita Book', 'balance': 120},
        'USER886': {'id': 'USER886', 'name': 'Robin Graves', 'balance': 80000}, # Robin Banks' partner
        'USER887': {'id': 'USER887', 'name': 'Rocky Beach', 'balance': 40},
        'USER888': {'id': 'USER888', 'name': 'Roman Holiday', 'balance': 5000},
        'USER889': {'id': 'USER889', 'name': 'Rose Bush', 'balance': 250},
        
        # The Grand Finale
        'USER890': {'id': 'USER890', 'name': 'Russell Sprout', 'balance': 75},
        'USER891': {'id': 'USER891', 'name': 'Sal Mon', 'balance': 850},
        'USER892': {'id': 'USER892', 'name': 'Sandy Banks', 'balance': 3000},
        'USER893': {'id': 'USER893', 'name': 'Sara Tonin', 'balance': 1000},
        'USER894': {'id': 'USER894', 'name': 'Saul T. Nuts', 'balance': 15},
        'USER895': {'id': 'USER895', 'name': 'Stan Dupp', 'balance': 200},
        'USER896': {'id': 'USER896', 'name': 'Sue Shi', 'balance': 600},
        'USER897': {'id': 'USER897', 'name': 'Terry Bull', 'balance': 2},
        'USER898': {'id': 'USER898', 'name': 'Ty Knotts', 'balance': 500},
        'USER899': {'id': 'USER899', 'name': 'Will Power', 'balance': 100000},
        'USER900': {'id': 'USER900', 'name': 'Archit Krish', 'balance': 100000000},
        'USER901': {'id': 'USER901', 'name': 'Ameed', 'balance': 75000},
        'USER902': {'id': 'USER902', 'name': 'Justin Case', 'balance': 15000},
        'USER945': {'id': 'USER945', 'name': 'Robin Banks', 'balance': 850000},
        'USER999': {'id': 'USER999', 'name': 'Penny Pincher', 'balance': 5},
        
        # The Wealthy Tech Moguls
        'USER1024': {'id': 'USER1024', 'name': 'Elon Tusk', 'balance': 250000000000},
        'USER1100': {'id': 'USER1100', 'name': 'Richie Rich', 'balance': 1000000000},
        'USER1150': {'id': 'USER1150', 'name': 'Scrooge McDuck', 'balance': 999999999999},
        
        # The Secret Agents
        'USER007': {'id': 'USER007', 'name': 'Kiwu Raj', 'balance': 7000000},
        'USER1200': {'id': 'USER1200', 'name': 'Ethan Hunt', 'balance': 2500000},
        'USER1212': {'id': 'USER1212', 'name': 'Jason Bourne', 'balance': 45000},
        
        # The "Broke" Accounts
        'USER1300': {'id': 'USER1300', 'name': 'Anita Break', 'balance': 10},
        'USER1350': {'id': 'USER1350', 'name': 'Phil McCracken', 'balance': 2},
        'USER1390': {'id': 'USER1390', 'name': 'Broke McPoor', 'balance': 0.50}
    }
        self.user_log = {
        # Punny Accounts
        "USER902": [f"Logged in at: {datetime.datetime(2026, 3, 20, 10, 15)}", f"Withdrew 200Rs at: {datetime.datetime(2026, 3, 21, 11, 0)}"],
        "USER945": [f"Logged in at: {datetime.datetime(2026, 3, 20, 14, 30)}", f"Withdrew 500Rs at: {datetime.datetime(2026, 3, 22, 0, 5)}"],
        "USER999": [f"Deposited 5Rs at: {datetime.datetime(2026, 3, 21, 9, 5)}"],
        
        # Wealthy Tech Moguls
        "USER1024": [f"Deposited 1000000Rs at: {datetime.datetime(2026, 3, 21, 11, 20)}"],
        "USER1100": [f"Withdrew 50000Rs at: {datetime.datetime(2026, 3, 22, 16, 45)}"],
        "USER1150": [f"Deposited 99999Rs at: {datetime.datetime(2026, 3, 22, 18, 0)}"],
        
        # Secret Agents
        "USER007": [f"Mission briefing login at: {datetime.datetime(2026, 3, 23, 0, 7)}"],
        "USER1200": [f"Withdrew 2000Rs at: {datetime.datetime(2026, 3, 23, 8, 12)}"],
        "USER1212": [f"Identity verification at: {datetime.datetime(2026, 3, 23, 13, 55)}"],
        
        # Broke Accounts
        "USER1300": [f"Withdrew 10Rs at: {datetime.datetime(2026, 3, 24, 10, 30)}"],
        "USER1350": [f"Deposited 100Rs at: {datetime.datetime(2026, 3, 24, 12, 15)}"],
        "USER1390": [f"Withdrew 1Rs at: {datetime.datetime(2026, 3, 24, 15, 45)}"]
    }
    def login(self):
        usr = input('Are you an existing user? (Y/N): ').upper()
        if usr == 'Y':
            self.info_user = {
                'id': input('Input your id: ').upper(),
                'name': input('Enter you name: ').title()
            }
            user_id = self.info_user.get('id')
            if user_id in self.user_base:
                stored_user = self.user_base[user_id]
                if stored_user['name'] == self.info_user['name']:
                    print(f'Welcome {stored_user["name"]}!\n')
                    if user_id not in self.user_log:
                        self.user_log[user_id] = []
                    self.user_log[user_id].append(f'Logged in at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
                    self.current_user = user_id
                    return True
                else:
                    print('ID or Name is incorrect. Please try again.')
            else:
                print('No such user was found in our database!')
        elif usr == 'Y':
            print('Welcome to our bank! Please create your account through our app and enjoy our services!')
        else:
            print('No bank credentials found!')
        return False
    def withdraw(self):
        try:
            amount = float(input('\nInput amount to be withdrawn: '))
        except ValueError:
            print('\nInvalid number found!')
            return
        
        current_balance = self.user_base[self.current_user]['balance']   
        if amount > current_balance:
            print('Insufficient funds!')
        elif amount == current_balance:
            print('\nLast call! After this, your vault is officially empty.')
            confirm = input('Do you still want to proceed? (Y/N)').upper()
            if confirm == 'Y':
                self.user_base[self.current_user]['balance'] -= amount   
                print(f'Transaction successful ! Your current balance is: {self.user_base[self.current_user]['balance']}')
                self.user_log[self.current_user].append(f'{amount}Rs. withdrawn at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
            else:
                print('\nHurrah ! You saved your account from going dry.')
        else:
            self.user_base[self.current_user]['balance'] -= amount
            print(f'Your current balance is: {self.user_base[self.current_user]['balance']}')
            self.user_log[self.current_user].append(f'{amount}Rs. withdrawn at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')

    def deposit(self):
        try:
            amount = float(input('\nKindly input amount you want to deposit: '))
        except ValueError:
            print('\nInvalid input!')
        if amount <= 0:
            print('\nDeposit must be greater than zero!')
        else:
            self.user_base[self.current_user]['balance'] += amount
        print(f'Deposit successful! \nYour current balance is: {self.user_base[self.current_user]['balance']}')
        self.user_log[self.current_user].append(f'{amount}Rs. deposited at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')

    def check_balance(self):
        current_balance = self.user_base[self.current_user]['balance']
        print(f'Your current balance is: {current_balance}')
        self.user_log[self.current_user].append(f'{self.info_user['name']}\'s Balance checked at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')

    def check_logs(self):
        if self.current_user in self.user_log:
            all_logs = sorted([log for log_list in self.user_log.values() for log in log_list])
            all_logs_string = '\t\n'.join(all_logs)
            print('Your bank logs:\n\n', all_logs_string)
            self.user_log[self.current_user].append(f'Bank log generated to view at: {datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")}')
        elif self.current_user not in self.user_log:
            print('Oops! no log history to show...\nCongrats, this is your first log via our online Bank')
            self.user_log[self.current_user].append(f'1st Bank log generated to view at: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
        else:
            print('An unknown error occured! Please try after some time...')
        
my_bank = Bank()
if my_bank.login():
    while True :
        print('\nWhat would you like to do today?')
        print('------ATM Menu------ \n1. Withdraw \n2. Deposit\n3. Check Balance\n4. Check history\n5. Logout\n')
        try:
            choice = int(input('Enter your choice (1-5): '))
            if choice == 1:
                my_bank.withdraw()
                confirm = input('\nWould you like to logout? (Y/N): ').upper()
                if confirm == 'Y':
                    print('Logout successful! \nHave a great day...\n\tReturning to main menu....')
                    my_bank.current_user = None
                    my_bank.login()  
                elif confirm == 'N':
                    print('\nWhat would you like to do?')
                else:
                    print('An unknown error occured. Please try again!')
                    
            elif choice == 2:
                my_bank.deposit()
                confirm = input('\nWould you like to logout? (Y/N): ').upper()
                if confirm == 'Y':
                    print('Logout successful! \nHave a great day...\n\tReturning to main menu.... ')
                    my_bank.current_user = None
                    my_bank.login()
                elif confirm == 'N':
                    print('\nWhat would you like to do?')
                else:
                    print('An unknown error occured. Please try again!')
                
            elif choice == 3:
                my_bank.check_balance()
                confirm = input('\nWould you like to logout? (Y/N): ').upper()
                if confirm == 'Y':
                    print('Logout successful! \nHave a great day...\n\tReturning to main menu....')
                    my_bank.current_user = None
                    my_bank.login()
                elif confirm == 'N':
                    print('\nWhat would you like to do?')
                else:
                    print('An unknown error occured. Please try again!')
                
            elif choice == 4:
                my_bank.check_logs()
                confirm = input('\nWould you like to logout? (Y/N): ').upper()
                if confirm == 'Y':
                    print('Logout successful! \nHave a great day...\n\tReturning to main menu....')
                    my_bank.current_user = None
                    my_bank.login()
                elif confirm == 'N':
                    print('\nWhat would you like to do?')
                else:
                    print('An unknown error occured. Please try again!')
                
            elif choice == 5:
                my_bank.current_user = None
                print('\nLogout/Exit successful! Have a great day!')
                break
            else:
                print('\nInvalid choice! Please try again.')
        except ValueError:
            print('\nInvalid input! Please enter 1, 2, 3, 4 or 5.')
else:
    print('\nSomething went wrong....Try again!')
    


        
        
        
        
        
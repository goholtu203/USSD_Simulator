
welcome_message = '''	 

			 _______________________
			|	Welcome		|
			|     To Our USSD	|
			|	Service		|
			|Select(1-5) For your 	|
			| desired option...	|
			| 1. Buy airtime	|
			| 2. Buy data		|
			| 3. Borrow airtime/data|
			| 4. Check Balance	|
			| 5. Exit		|
			|_______________________|

'''
ussd = "*555#"
account_balance=50
enter_ussd = input()
if enter_ussd == ussd:
	while True:
		menu=input(welcome_message)
# Buy Airtime
		if menu == "1":
			phone_number=input("Enter Destination Phone Number: ")
			if len(phone_number)==11:
				amount= int(input("Enter Amount: "))
				if amount < account_balance:
					print(f"You have Succesfully Buy {amount} airtime to {phone_number} and your balane is{account_balance-amount}")
					break
				else:
					print("Insufficient balance to perform transaction")
			else: 
				print("Invalid Phone number")	

#Buy data
		elif menu == "2":
			phone_number = input("Enter destination phone number: ")
			if len(phone_number) == 11:
				data_menu = '''
				select plan:
				1. 1GB -- 500
				2. 2GB -- 800
				3. 3GB -- 1000	
				'''
				_1GB= 500
				_2GB= 800
				_3GB= 1000
				data_plan = input(data_menu)
				if data_plan == "1":
					if _1GB < account_balance:
						print(f"You have successfully buy 1GB worth {_1GB} and your balance left is {account_balance - _1GB}")
					else:
						print("Insufficient Balance")
				elif data_plan == "2":
					if _2GB < account_balance:
						print(f"You have successfully buy 1GB worth {_2GB} and your balance left is {account_balance - _2GB}")
					else:
						print("Insufficient Balance")
				elif data_plan == "3":
					if _3GB < account_balance:
						print(f"You have successfully buy 1GB worth {_3GB} and your balance left is {account_balance - _3GB}")
					else:
						print("Insufficient Balance")
				else:
					print("Invalid option, Choose from 1-3")
			else:
				print("Invalid Phone number")
#borrow airtime /data
		elif menu == "3":
			print( '''
				select:
				1. Borrow airtime
				2. Borrow data
			''')
			borrow_option=input("select option: ")
			if borrow_option=="1" and account_balance<100:
				phone_number=input("Enter phone number; ")
				if len(phone_number):
					borrow_amount=input("Enter Amount to borrow: ")
					print(f"You have successfully borrowed {borrow_amount} on {phone_number}")
				else:
					print("Invalid Phone number")
			elif borrow_option == "2" and account_balance<100:
				phone_number = input("Enter phone number")
				if len(phone_number) ==11:
					print('''
					1. 1gb -- 500
					2. 2gb -- 800
					3. 3gb -- 1000
					''')
					plan_to_borrow = input()
					if plan_to_borrow == "1":
						print(f"You have successfully borrow 1gb worth 500")
					elif plan_to_borrow == "2":
						print("You have sucessfully borrowed 2bg worth 800")
					elif plan_to_borrow == "3":
						print("You have succesfully borrowed 3bg wortth 1000")
					else:
						print("invalid option(choose from option 1-3)")

				else:
					print("Invalid phone number")
			else:
				print(f"Yuor account balance is still {account_balance} so you cant borrow.. You can buy airtime / data")
		elif menu == "4":
			print(f"You account balance is {account_balance}")
		elif menu == "5":
			print("Thank you for using our USSD")
			break
		else:
			print("invalid input(Number must be between 1-5)")



else:
	print("Sorry You entered the code, dail *555# and try again")




























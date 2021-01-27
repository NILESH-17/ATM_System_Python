banking=True
cust1={"name":"mark","password":1234, "balance":15000}
cust2={"name":"tom","password":1705, "balance":50000}
while banking==True:

	user_input=int(input(""" enter a choice:
 1)credit
 2)debit
 3)balance
 4)help
   """))
	if user_input==int(1):
		password=int(input("enter a password "))
		if password==cust1["password"]:
			print("welcome, mark.. please enter an amount you want to deposit: ")
			amount_to_deposit=int(input("enter an amount: "))
			new_balance=amount_to_deposit+cust1["balance"]
			print(f"{amount_to_deposit} rs deposited into your acc..new_balance is {new_balance} rs")
		elif password==cust2["password"]:
			print("Welcome,tom....please enter an amount to be deposit: ")
			amount_to_deposit=int(input("enter an amount: "))
			new_balance=amount_to_deposit+cust1["balance"]
			print(f"{amount_to_deposit} rs deposited into your acc..new balance is {new_balance} rs")
		else:
			print('Enter valid Password')






	if user_input==int(2):
		password=int(input("enter a password "))
		if password==cust1["password"]:
			print("welcome, mark.. please enter an amount you want to debit: ")
			amount_to_debit=int(input("enter an amount: "))
			if amount_to_debit > cust1["balance"]:
				print(f"insuffient funds...availabale balance is {balanced} rs")
			else:

			 new_balance= cust1["balance"] - amount_to_debit
			 print(f"{amount_to_debit} rs debited from your acc..new balance is {new_balance} rs")
		elif password==cust2["password"]:
			print("Welcome,tom....please enter an amount to be debit: ")
			balanced=cust2["balance"]
			amount_to_debit=int(input("enter an amount: "))
			if amount_to_debit > cust2["balance"]:
				print(f"insuffient funds...availabale balance is {balanced} rs")
			else:

			 new_balance= cust2["balance"] - amount_to_debit
			 print(f"{amount_to_debit} rs debited from your acc..new balance is {new_balance} rs")
		else:
			print('Enter valid Password')

	if user_input==int(3):
		password=int(input("enter your password "))
		if password==cust1["password"]:
			print(cust1["balance"])
		elif password==cust2["password"]:
			print(cust2["balance"])
		else:
			print("Please enter a Valid Password")

	if user_input==int(4):
		print("please visit to our nearest branch for further Enquiries")




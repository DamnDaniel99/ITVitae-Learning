"""

Expand on the contacts app from a few scripts ago.
1. Write a similar contact managing app as before. However, this time, store contact data in a list of dictionaries,
as shown below:
[{'name': <NAME>, 'phone': <PHONE>, 'email': <EMAIL>}]

Expand on the previous script.
1. Make a copy of the previous script.
2. Add functionality to the program:
i. Allow to display a single user's data by entering their email address or list index number. Use a loop and
in to find the right user.
ii. Allow for the removal of a single user by entering their email address or list index number. Use a loop and
in to find the right user.

"""

def Welcome():
	Action = int(input('''
		Welcome!
		What would you like to do?
		Press:
		1 for List entries
		2 for Add entry
		3 for View entry
		4 for Delete entry
		5 for Exit Phonebook
		'''))
	return Action


def Phonebook():
	#Empty contact list to store values
	contacts = {}

	#This is a while loop to continously run the phonebook function
	while True:
		Action = Welcome()

		#Conditions for decision making for any option entered by the user
		if Action == 1:
			#First it's checking if the contact list is empty
			#If not empty, it prints the current contact list
			if bool(contacts) != False:
				for k, v in contacts.items():
					print(k, ':', v)
			#Else inform the user that the contact book is empty
			else:
				print('This phonebook is empty!')

		#Decision for the second entry
		elif Action == 2:
			#Request for a name, phone number and email address
			name = input('What is your name? ')
			phone = input('What is your phone number? ')
			email = input('What is your email address? ')

			#Here is a new variable contact to create a new dict to put in to the dict Contacts
			contact = str({'Name':[name], 'Email Address':[email], 'Phone Number':[email]})

			#Check if the data already exists in the Phonebook
			#If it doesn't exists, update the contact list in Phonebook
			if contact not in contacts:
				contacts['Name'].append(name)
				contacts['Email Address'].append(email)
				contacts['Phone Number'].append(phone)
				#Printing a success message
				print('Contact succesfully saved!')
				print('Your updated phonebook is shown below: ')
				#Looping through the phonebook and display each contact in a seperate line
				for k, v in contacts.items():
					print(k, ':', v)
			#Else display a message to inform the user that contact already exists
			else:
				print('That contact already exists!')

		elif Action == 3:
			#Initiating a name variable that a user can look at
			email = input("What is the email address of the contact you are requesting? ")
			#A condition to check if the entered name is in the contact dictionairy
			if email in contacts:
				print("The contact's email address is",email,':',contacts[email])

			#Else inform them that the contact does not exist
			else:
				print('This contact does not exist')
		elif Action == 4:
			#Initiating the name variable 
			email = input('What is the email address of the contact you wish to delete? ')
			#Check if the contact exists
			if email in contacts:
				#print the required contact
				print("The contact's email address is",email,':',contacts[email])
				#Confirm whether the user wishes to delete the contact
				confirm = input("Are you sure you wish to delete this contact? Yes/No: ")
				#Intitiate a decision
				if confirm.capitalize() == 'Yes':
				#If yes, delete the contact from the phonebook
					contacts.pop(email,None)
					print("Your update phonebook is shown below:")
				#Loop through the phonebook and print update contact list
				for k, v in contacts.items():
					print(k, ":", v)
				#Else return to main menu
				else:
					print('Return to main menu')

			#Else inform display a message to inform the user that the contact does not exist
			else:
				print('This contact does not exist!')

		#Break program for the last action
		elif Action == 5:
			print('Thanks for using this Phonebook')
			break

		#Error message
		else:
			print('This action is not possible!')



		#End of program

Phonebook()
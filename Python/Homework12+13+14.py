"""

Expand on the previous script.
1. Allow for the storage of several phone numbers (hint: store them as a dict would allow for naming entries
easily).
2. Allow for the storage of several additional email addresses by expanding the basic user dict to include a
secondary_emails key.

Expand on the previous script.
1. Implement search by name functionality:
Search by name using a loop and in .
Store search results in a list.
Print search results on seperate lines and include their main identifiers (list index number and email address)

Write a perfect little contact managing application that makes use of unique identifiers, has search functionality and
can write data to disk.
1. Write a contact managing tool as before, however, this time, store contact data in dicts in a dict. The main dict
uses a contact's main email addresses as the unique identifier.
{'<EMAIL>': {'name': <NAME>, 'phone_numbers': <PHONE_NUMBERS>, 'emails': <ALT_EMAILS>}}
2. Adding contacts or displaying a specific contact's data should be done through their email address.
3. Implement a name search as before.
4. Allow for writing the main dictionary to a file.
5. Implement a way to load the main dict.
6. Add extra fields to your whishes or liking. Consider the data typing per field (for example, address: most
contact managers support several named address fields).

"""

Phonebook = { 
				'{pri_email}': {'name': {name}, 'phone_numbers': {phone_number}, 'emails': {sec_email}}
			}

#Writing the main dict to a file.
#import json
#with open('Phonebook.txt', 'a') as file:
	#file.write(json.dumps(Phonebook))

#Reading the main dict from a file.
#import json
#with open('Phonebook.txt') as file:
	#file.read(json.loads(Phonebook))

#Import pprint function of the pprint module
#from pprint import pprint

Action = int(input('''
	Welcome!
	What would you like to do?
	Press:
	1 for List entries
	2 for Add entry
	3 for View entry
	4 for Delete entry
	5 for Search
	6 for Exit Phonebook
'''))



def list_entries():
	#Storage of the entries should be a nested dictionary, using a main email address as the unique identifier.
	pass

def add_entry():
	#It should be possible to add several phone numbers and email addresses.
	pass

def view_entry():
	#This should be done through their email addresses or list index numbers.
	pass

def delete_entry():
	#This should be done through their email addresses or list index numbers. Use the .pop() method.
	pass

def search():
	#Searching should be done using a loop and 'in'.
	#Results should be stored in a list and printed on seperate lines.
	#Printed results should include their main identifiers - list index numbers & email addresses
	pass

def exit_phonebook():
	print('Thanks for using this Phonebook')



while Action != '6':

	if Action == '1':
		list_entries()

	elif Action == '2':
		add_entry()

	elif Action == '3':
		view_entry()

	elif Action == '4':
		delete_entry()

	elif Action == '5':
		search()

	elif Action == '6':
		exit_phonebook()
		break



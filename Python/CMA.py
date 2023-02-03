"""
Simple Contact managing app.
"""

class Phonebook:
	'''DOC'''

	def __init__(self):
		'''Initialization.'''
		self.data = {}

	def print_contacts(self):
		'''Prints the contact in a dictionairy.'''
		print(self.data)

	def add_contact(self):
		'''Gives the option to add contacts to the dictionairy.'''
		x = input('''Please insert the contact name: ''').lower()
		self.data.update({x:x})

	def delete_contact(self):
		'''Gives the option to remove contacts from the dictionairy'''
		x = input('''Please insert the contact name: ''').lower()
		self.data.pop(x)
		print('''Contact Deleted!''')
		print(self.data)

	def search_contact(self):
		'''Gives the option to search contact in the dictionairy.'''
		x = input('''Please insert the contact name: ''').lower()
		result = self.data.get(x)
		print('''The contact is: ''', result)
"""
Simple Contact managing app.
"""

class Phonebook:

	def __init__(self):
		self.data = {}

	def print_contacts(self):
		print(self.data)

	def add_contact(self):
		x = input().lower()
		self.data.update({x:x})

	def delete_contact(self):
		x = input().lower()
		self.data.pop(x)
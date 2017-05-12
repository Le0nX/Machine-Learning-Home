import json

def greet_user():
	"""Greets user by name"""
	filename = 'user.json'
	try:
		with open(filename, 'r') as fle:
			name = json.load(fle)
	except FileNotFoundError:
		name = input("Hi! You are not in our lists. Enter your name: ")
		with open(filename, 'w') as fles:
			json.dump(name, fles)
		print("Ok, we'll remember you, " + name)
	else:
		print("Welcome back, " + name + "! Glad to see you again!")

greet_user()
#!/bin/python3
from argon2 import PasswordHasher
ph = PasswordHasher()

username = input("Enter username: ")
password = input("Enter password: ")

file = open('password.txt', "r")
for line in file:
    if username in line:
    	hashedPassword = line.split(username + ":")[1]
    	
    	try:
    		print(ph.verify(hashedPassword, password))
    	except:
    		print(False)
    	

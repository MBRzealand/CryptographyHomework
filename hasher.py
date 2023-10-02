#!/bin/python3
from argon2 import PasswordHasher
ph = PasswordHasher()

username = input("Enter username: ")
password = input("Enter password: ")

hashedPass = ph.hash(password)

with open('password.txt', 'w') as f:
    f.write(username + ":" + hashedPass)

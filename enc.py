#!/usr/bin/env python2
import binascii
def encrypt():
	text = raw_input("Please input your information to encrypt: ")
	for char in text:
		#Convert text into a binary sequence
		char = bin(int(binascii.hexlify(char),16))
	key = raw_input("Please input your key for decryption: ")
	for char in key:
		#Convert key into a binary sequence
		char = bin(int(binascii.hexlify(char),16))
	#This is only here for developmental purposes
	print key


		

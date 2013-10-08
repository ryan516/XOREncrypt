#!/usr/bin/env python2
import binascii
def encrypt():
	text = raw_input("Please input your information to encrypt: ")
	text = text.split(,)
	for char in text:
		char = bin(int(binascii.hexlify(char),16))
	key = raw_input("Please input your key for decryption: ")
	key = key.split(,)
	for char in key:
		char = bin(int(binascii.hexlify(char),16))

	print key


		

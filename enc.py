#!/usr/bin/env python3
import sys
from itertools import cycle

def encrypt():
  input_text = input("Please input your information to encrypt: ")

  key = input("Please input your key for decryption: ")

  #Verification String
  print("The text is '{}'".format(input_text))
  print("The key is '{}'".format(key))
  userInput1 = input("Is this information ok? y/n ")
  if userInput1 == 'y':
  	print("I am encrypting your data, please hold on.")
  elif userInput1 == 'n':
  	print("Cancelled your operation.")
  else:
  	print("I didn't understand that. Please type y or n (I do not accept yes or no as an answer, and make sure you type it in as lowercase. We should be able to fix this bug soon.)")
  
  if userInput1 == 'y': 
      print(''.join(map(lambda a, b: chr(ord(a) ^ ord(b)),
          input_text, cycle(key))))

encrypt()

#!/usr/bin/env python2
import sys
def encrypt():
  input_text = raw_input("Please input your information to encrypt: ")

  key = raw_input("Please input your key for decryption: ")

  #Verification String
  print "The text is '{}'".format(input_text)
  print "The key is '{}'".format(key)
  userInput1 = raw_input("Is this information ok? y/n ")
  if userInput1 == 'y':
  	print "I am encrypting your data, please hold on."
  elif userInput1 == 'n':
  	print "Cancelled your operation."
  else:
  	print "I didn't understand that. Please type y or n (I do not accept yes or no as an answer, and make sure you type it in as lowercase. We should be able to fix this bug soon.)"
  
  if userInput1 == 'y':
      chars = []
      for i, c in enumerate(input_text):
          chars.append(chr(ord(c) ^ ord(key[i%len(key)])))
      
      print(''.join(chars))




      



encrypt()

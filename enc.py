#!/usr/bin/env python2
def encrypt():
  text1 = raw_input("Please input your information to encrypt: ")
  text2 = []
  #Convert text1 into binary (text2)
  for char in text1:
    text2.append(bin(ord(char))[2:])
  text2 = ''.join(text2)

  key = raw_input("Please input your key for decryption: ")
  decryptionKey = []
  #Convert key into binary (decryptionKey)
  for char in key:
    decryptionKey.append(bin(ord(char))[2:])
  decryptionKey = ''.join(decryptionKey)

  #Verification String
  print "The text is '%s'" %text1
  print "The key is '%s'" %key
  userInput1 = raw_input("Is this information ok? y/n ")
  if userInput1 == 'y' or 'Y':
  	print "I am encrypting your data, please hold on."
  elif userInput1 == 'n' or 'N':
  	print "Cancelled your operation."
  else:
  	print "I didn't understand that. Please type y or n (I do not accept yes or no as an answer.)"

encrypt()
#!/usr/bin/env python2
import sys
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
  if userInput1 == 'y':
  	print "I am encrypting your data, please hold on."
  elif userInput1 == 'n':
  	print "Cancelled your operation."
  else:
  	print "I didn't understand that. Please type y or n (I do not accept yes or no as an answer, and make sure you type it in as lowercase. We should be able to fix this bug soon.)"

  finalString = []

  if userInput1 == 'y':
    for i in text2:
      j = 0
      k = 0
      val1 = text2[i] + decryptionKey[j]
      if val1 == 0:
        finalString[k] = 0
      elif val1 == 1:
        finalString[k] = 1
      elif val1 == 2:
        finalString[k] = 0
      j += 1
      k += 1
    print finalString




      



encrypt()
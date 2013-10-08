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

  print "The key is '%s'" %decryptionKey
  print "The text is '%s'" %text2

encrypt()



		

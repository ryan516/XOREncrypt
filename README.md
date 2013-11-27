==README

I am a simple encryption program written in Python, converting your Ascii Character input into a Binary Value, and XORing it with your Key's Binary Values.

## Example usage ##

### Encryption ###

```sh
$ ./enc.py 
Please input your information to encrypt: ABCDEF
Please input your key for decryption: efg
The text is 'ABCDEF'
The key is 'efg'
Is this information ok? y/n y
I am encrypting your data, please hold on.
$$$!#!
```

### Decryption ###

```sh
$ ./enc.py 
Please input your information to encrypt: $$$!#!
Please input your key for decryption: efg
The text is '$$$!#!'
The key is 'efg'
Is this information ok? y/n y
I am encrypting your data, please hold on.
ABCDEF
```

# Rijndael
# CSC 444 - Applied Cryptography
# Program #6 AES (Rijndael)
# Dr. Jean Gourd - 5/6/2020
# Ammar Essajee

from sys import stdin
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import re

# the AES block size to use
BLOCK_SIZE = 16
# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"
# the key to use in the cipher
#KEY = "heartburn"
# set reversed to 'True' to parse through the dictionary backwards
REVERSED = False
# set threshold to adjust accuracy of words in dictionary
THRESHOLD = 0.01
# SELECT WHICH CIPERTEXT FILE YOU ARE USING:
# specify cipher text number (1, 2, 3, 4, or 5) 
CIPHERTEXT = 4

if CIPHERTEXT == 1 or CIPHERTEXT ==2 or CIPHERTEXT == 3:
    # read dictionary.txt file and create an array of all words in dictionary.txt
    f = open("dictionary.txt", "r")
    dictionary = f.read().rstrip("\n").split("\n")
    f.close()

elif CIPHERTEXT == 4:
    # read dictionary.txt file and create an array of all words in dictionary.txt
    f = open("dictionary.txt", "r")
    dictionary = f.read().rstrip("\n").split("\n")
    f.close()

else:
    # read dictionary.txt file and create an array of all words in dictionary.txt
    f = open("dictionary5.txt", "r")
    dictionary = f.read().rstrip("\n").split("\n")
    f.close()

    

# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# get the 16-byte IV from the ciphertext
	# by default, we put the IV at the beginning of the ciphertext
	iv = ciphertext[:16]

	# decrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# the ciphertext is after the IV (so, skip 16 bytes)
	plaintext = cipher.decrypt(ciphertext[16:])

	# remove potential padding at the end of the plaintext
	plaintext = plaintext[:-16] + re.sub(r'[#]','', plaintext[-16:])

	return plaintext

# encrypts a plaintext with a key
def encrypt(plaintext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# generate a random 16-byte IV
	iv = Random.new().read(BLOCK_SIZE)

	# encrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# if necessary, pad the plaintext so that it is a multiple of BLOCK SIZE in length
	plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
	# add the IV to the beginning of the ciphertext
	# IV is at [:16]; ciphertext is at [16:]
	ciphertext = iv + cipher.encrypt(plaintext)

	return ciphertext

# MAIN
plaintext = stdin.read().rstrip("\n")
ciphertext = plaintext

# check dictionary if keyword matches
if REVERSED == True:
    dictionary = reversed(dictionary)

for keyword in dictionary:
    if CIPHERTEXT == 1 or CIPHERTEXT == 2 or CIPHERTEXT == 3:
        # decrypt message using current key
        ciphertext.encode("base64").replace("\n", "")
        plaintext = decrypt(ciphertext, keyword)
        # split plaintext into list of words
        words = plaintext.split(" ")

        # remove punctuation from words
        words = [s.strip(".") for s in words]
        words = [s.strip("!") for s in words]
        words = [s.strip(",") for s in words]
        words = [s.strip("?") for s in words]
        words = [s.strip('"') for s in words]
        words = [s.strip("'") for s in words]


        count = 0
        # check if word in plaintext is in dictionary
        for word in words:
            if word in dictionary:
                # increase count if match occurs
                count = count + 1
        # find appropriate candidate text
        # switch '<' to '>' to find accurate plaintext
        if count > len(words) * THRESHOLD:
            print "KEY={}".format(keyword) 
            print plaintext

    if CIPHERTEXT == 4:
        keyword = keyword + '$'
        # decrypt message using current key
        ciphertext.encode("base64").replace("\n", "")
        plaintext = decrypt(ciphertext, keyword)
        # split plaintext into list of words
        words = plaintext.split(" ")

        # remove punctuation from words
        words = [s.strip(".") for s in words]
        words = [s.strip("!") for s in words]
        words = [s.strip(",") for s in words]
        words = [s.strip("?") for s in words]
        words = [s.strip('"') for s in words]
        words = [s.strip("'") for s in words]


        count = 0
        # check if word in plaintext is in dictionary
        for word in words:
            if word in dictionary:
                # increase count if match occurs
                count = count + 1
        # find appropriate candidate text
        # switch '<' to '>' to find accurate plaintext
        if count < len(words) * THRESHOLD:
            print "KEY={}".format(keyword) 
            print plaintext

    if CIPHERTEXT == 5:
        # decrypt message using current key
        ciphertext.encode("base64").replace("\n", "")
        plaintext = decrypt(ciphertext, keyword)
        # split plaintext into list of words
        words = plaintext.split(" ")
        if plaintext[0] == "%" and plaintext[1] == "P" and plaintext[2] == "D" and plaintext[3] == "F":
            print plaintext
            

            
            

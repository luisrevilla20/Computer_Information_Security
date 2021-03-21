import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
from Crypto.Cipher import  AES
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Step 1 Connect to the server
s.connect(('54.226.141.110', 13337))

#Step 2 Send Hello msg
plaintext = b'Hello!RSA-AES'
s.send(plaintext)

#Step 3 Receive Public Key
data = s.recv(1024)
print(data.decode("ascii"))

#Step 4 Import publicx key and create PKCS instance
f=open("publickey.pem", "rb")
key=RSA.import_key(f.read())
f.close()
pkcsInstance=PKCS1_OAEP.new(key)

#Step 5 Create key and iv
key=b'ayudenosprofe!!!'
iv=b'profeayudenos!!!'
key_iv= b'ayudenosprofe!!!,profeayudenos!!!'

#Step 6  Send the encrypted key and iv 
cipherkey_iv=pkcsInstance.encrypt(key_iv)
s.send(cipherkey_iv)

#Step 7 Create 2 instances of AES (1 to encrypt 1 to decrypt)
aes_decryptInstance=AES.new(key, AES.MODE_CBC, iv)
aes_encryptInstance=AES.new(key, AES.MODE_CBC, iv)

#Step 8 receive message (Send your names!!)
data2 = s.recv(1024)
print(data2)
aes_decrypt=aes_decryptInstance.decrypt(data2)
print(aes_decrypt.decode("ascii"))


#Step 9 Create a message with teammates names (16 bit multiple)
name_message=b'luisorevillayjesusgonzaleza!!!!!' #32 bits

#Step 10 Combine key_iv with name_message and hash it
digest=hashlib.sha256()
digest.update(b"".join([key, name_message]))
r=digest.digest()

#Step 11 Combine the name with the hash
name_hash=b"".join([name_message, r])
aes_encrypt=aes_encryptInstance.encrypt(name_hash)
s.send(aes_encrypt)

#Step 12 Receive validation message
data3= s.recv(1024)
aes_decrypt=aes_decryptInstance.decrypt(data3)
print(aes_decrypt.decode("ascii"))


s.close()

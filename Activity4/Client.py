import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
from Crypto.Cipher import  AES

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plaintext = b'Hello!RSA-AES'
s.connect(('54.226.141.110', 13337))
s.send(plaintext)
data = s.recv(1024)
print(data.decode("ascii"))

f=open("publickey.pem", "rb")
key=RSA.import_key(f.read())
f.close()
pkcsInstance=PKCS1_OAEP.new(key)

key=b'ayudenosprofe!!!'
iv=b'profeayudenos!!!'
key_iv= b'ayudenosprofe!!!,profeayudenos!!!'
cipherkey_iv=pkcsInstance.encrypt(key_iv)
s.send(key_iv)

aesInstance=AES.new(key, AES.MODE_CBC, iv=iv)
#aes_decryptInstance=AES.new(key, AES.MODE_CBC, iv)
#aes_encryptInstance=AES.new(key, AES.MODE_CBC, iv)
name_message=b'luisorevillayjesusgonzaleza!!!!!'
aes_encrypt=aesInstance.encrypt(name_message)
s.send(name_message)

data2 = s.recv(1024)
print(data2.decode("ascii"))
aes_decrypt=aesInstance.decrypt(data2)
print(aesInstance.decode("ascii"))

s.close()

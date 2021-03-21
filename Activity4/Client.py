import socket
from Crypto.Cipher import DES

#byte or 64 bits
key = b'thisis8b'
iv = b'iv8bits!'
# desInstance = DES.new(key, mode=DES.MODE_CBC, iv=iv)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plaintext = b'Hello!RSA-AES'
# ciphertext = desInstance.encrypt(plaintext)
s.connect(('54.226.141.110', 13337))
s.send(plaintext)
s.close()


import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#8 byte or 64 bits
f = open("public.pem", "rb")
key = RSA.import_key(f.read())
f.close()

rsaInstance = PKCS1_OAEP.new(key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plaintext = b'thisisamessage!!'
ciphertext=rsaInstance.encrypt(plaintext)
s.connect(('3.235.246.55', 1337))
s.send(ciphertext)
s.close()

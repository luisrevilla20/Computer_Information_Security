import socket
from Crypto.Cipher import DES

key=b'thisis8b'
iv=b'iv8bits!'
desInstance = DES.new(key, mode=DES.MODE_CBC, iv=iv)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plaintext = b'thisisamessage!!'
ciphertext=desInstance.encrypt(plaintext)
s.connect(('3.235.246.55', 1337))
s.send(ciphertext)
s.close()

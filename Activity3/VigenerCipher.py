from shift import letterdistance
from CaesarCipher import CaesarEncoder

#mode means if you want to decode or encode
#mode = True means you want to decipher
#mode = False means you want to cipher

file = open("cipher2.txt", "r")
cipher2 = file.read()

def VigenerEncoder(text, key, mode):
    result=""
    for i in range(len(text)):
        result += CaesarEncoder(text[i], letterdistance(key[i%4]), mode)
    return result


print(VigenerEncoder(cipher2, "yecv", True))
file.close()



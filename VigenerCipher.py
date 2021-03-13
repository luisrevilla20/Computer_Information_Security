from shift import letterdistance
from CaesarCipher import CaesarEncoder

def VigenerEncoder(text, key, mode):
    result=""
    keyLength = 0
    for i in range(len(text)):
        if keyLength == len(key):
            keyLength = 0
        result += CaesarEncoder(text[i], letterdistance(key[keyLength]), mode)
    return result


print(VigenerEncoder("Uftu tfoufodf #35", "bbbb", True))

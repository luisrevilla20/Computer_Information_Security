# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = int(input("Write the key for the Caesar decipher/cipher: "))

# encipher
def cipher(k, pt):
    ciphertext = ""
    for c in pt.upper():
        if c.isalpha():
            ciphertext += I2L[(L2I[c] + k) % 26]
        else:
            ciphertext += c
    return ciphertext

# decipher
def decipher(k, ct):
    plaintext2 = ""
    for c in ct.upper():
        if c.isalpha():
            plaintext2 += I2L[(L2I[c] - k) % 26]
        else:
            plaintext2 += c
    return plaintext2

def switch():
    answer = input("What do you want to do: cipher or decipher?: ")
    plaintext = ""
    ciphertext = ""

    if answer == 'cipher':
        plaintext = input("Write down the message you want to cipher: ")
        result = cipher(key, plaintext)

    elif answer == 'decipher':
        ciphertext = input("Write down the message you want to decipher: ")
        result = decipher(key, ciphertext)

    else:
        result = "Incorrect option"

    return result



r = switch()
print (r)


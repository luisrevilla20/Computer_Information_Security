import onetimepad
import random

def OneTimePad(plaintext):
    key = ""
    words = [["Two", "Three", "Four"],
            ["red", "yellow", "green"],
            ["cats", "dogs", "zebras"],
            ["jumped.", "danced.", "wrote_poetry."]]

    key = "".join([random.choice(w) for w in words])


    cipher = onetimepad.encrypt(plaintext, key)
    msg = onetimepad.decrypt(cipher, key)

    return msg, key, cipher

pad = OneTimePad("Pepitopepita")
print(pad)

from shift import shiftchar

#mode means if you want to decode or encode
#mode = True means you want to decipher
#mode = False means you want to cipher
# file = open("cipher1.txt", "r")
# cipher1 = file.read()
# letters ="abcdefghijklmnopqrstuvwxyz "

def CaesarEncoder(text, n, mode):
    result = ""
    for i in range(len(text)):
        if mode == False:
            result += shiftchar(text[i], n)
        else:
            result += shiftchar(text[i], (n*-1))
    return result
# alphabet = 27
# #print(CaesarEncoder(letters, 1, False))
# for i in range(alphabet):
#     print(CaesarEncoder(letters, i, False))
#     print("Linea: ", i)
#     print()
# file.close()



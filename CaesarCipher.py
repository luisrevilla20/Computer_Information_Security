from shift import shiftchar

#mode means if you want to decode or encode
#mode = True means you want to decode
#mode = False means you want to encode

def CaesarEncoder(text, n, mode):
    result = ""
    for i in range(len(text)):
        if mode == False:
            result += shiftchar(text[i], n)
        else:
            result += shiftchar(text[i], (n*-1))
    return result


# print(CaesarEncoder("Ymj 3 Wji $% Ynljwx", 5, True))



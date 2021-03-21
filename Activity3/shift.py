def shiftchar(letter, n):
    result = ""
    if n >= 26:
        n = n % 26
    if ord(letter) > 96 and ord(letter) < 123:
        if n > 0: 
            if (ord(letter) + n) > 123:
                result =  chr(ord(letter) - (26 - (n-1)))
            elif (ord(letter) + n) == 123:
                result = chr(32)
            else:
                result = chr(ord(letter) + n)
        elif n < 0:
            if (ord(letter) + n) < 96:
                result = chr(ord(letter) + (26 + (n+1)))
            elif (ord(letter) + n) == 96:
                result = chr(32)
            else:
                result = chr(ord(letter) + n)
        else:
            result = letter
    elif ord(letter) == 32:
        if n > 0:
            result = chr(96 + n)
        elif n < 0:
            result = chr(123 + n)
    else:
        result = letter
    return result


def letterdistance(letter):
    l = ord(letter)
    n = 0
    n = l - ord("a")

    return n


# print(letterdistance("c"))

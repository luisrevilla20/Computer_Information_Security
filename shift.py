def shiftchar(letter, n):
    if ord(letter) > 64 and ord(letter) < 91:
        if n > 0:
            if (ord(letter) + n) >= 91:
                return chr(ord(letter) - (26 - n))
            else:
                return chr(ord(letter) + n)
        elif n < 0:
            if (ord(letter) + n) <= 64:
                return chr(ord(letter) + (26 + n))
            else:
                return chr(ord(letter) + n)
        else:
            return letter
    elif ord(letter) > 96 and ord(letter) < 123:
        if n > 0:
            if (ord(letter) + n) >= 123:
                return chr(ord(letter) - (26 - n))
            else:
                return chr(ord(letter) + n)
        elif n < 0:
            if (ord(letter) + n) <= 96:
                return chr(ord(letter) + (26 + n))
            else:
                return chr(ord(letter) + n)
        else:
            return letter
    else:
        return letter


def letterdistance(letter):
    l = ord(letter)
    n = 0
    while l != 97:
        n += 1
        l -= 1

    return n


def decipher_message(message):
    if message == "":
        return ""
    lngth = int(len(message)**.5)
    splitted_message = [message[x:x+lngth] for x in range(0, len(message),lngth)]
    return ''.join([splitted_message[x][y] for y in range(len(splitted_message)) for x in range(lngth)])

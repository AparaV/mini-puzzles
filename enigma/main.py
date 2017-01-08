CODE = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
           'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
           'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
           'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
           'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
           'Z': 25}
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def isValid(text):
    for letter in text:
        if not letter.isalpha() and letter != ' ':
            return False
    return True

def encrypt(msg, key):
    if not isValid(msg) or not key.isalpha():
        print "Key and message should contain only letters from the alphabet"
        return False
    msg = msg.upper()
    key = key.upper()
    encrypted_text = ''
    i = 0
    length = len(key)
    for letter in msg:
        if letter == ' ':
            encrypted_text += ' '
            continue
        distance = CODE[key[i]]
        place = (distance + CODE[letter]) % 26
        encrypted_text += ALPHA[place]
        i = (i + 1) % length
    return encrypted_text
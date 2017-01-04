from pydub import AudioSegment

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

SOUNDPATH = './morse_sound_files/'
OUTPUTPATH = './output/'

def verify(message):
    keys = CODE.keys()
    for char in message.upper():
        if char not in keys:
            print char + ' not a valid character!'
            return False
    return True

def encode(message, fname):
    output = AudioSegment.empty()
    for char in message.upper():
        path = SOUNDPATH + char + '_morse_code.ogg'
        audio = AudioSegment.from_ogg(path)
        output += audio
    output.export(fname + '.mp3', format='mp3')
    print 'File generated to %s.mp3' %(fname)

def readfile(fname):
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip('\n')
            values = line.split(',')
            d[str(values[0])] = str(values[1])
    return d
    

if __name__ == "__main__":
    values = readfile('data.csv')
    print values
    for item in values:
        msg = values[item]
        if verify(msg) == True:
            encode(msg, OUTPUTPATH + item)
        else:
            print 'Message not valid.\nOnly letters and numbers are allowed. No special characters and spaces'
    print 'Morse code audio generated'

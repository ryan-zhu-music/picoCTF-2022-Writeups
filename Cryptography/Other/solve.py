def basic_mod1():
    import string
    message = "91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102"
    alphabet = string.ascii_lowercase + string.digits + "_"
    FLAG = "picoCTF{"
    for i in message.split():
        FLAG += alphabet[int(i) % 37]
    FLAG += "}"
    print("Flag:", FLAG)

def basic_mod2():
    import string
    message = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377"
    alphabet = string.ascii_lowercase + string.digits + "_"
    FLAG = "picoCTF{"
    for i in message.split():
        FLAG += alphabet[pow(int(i), -1, 41) - 1]
    FLAG += "}"
    print("Flag:", FLAG)

def credstuff():
    import string
    enc = "cvpbPGS{P7e1S_54I35_71Z3}"
    alphabet = string.ascii_lowercase
    FLAG = ""
    for i in enc:
        if i in string.digits + "{}_":
            FLAG += i
            continue
        FLAG += alphabet[(alphabet.index(i.lower()) + 13) % 26]
    print("Flag:", FLAG)

def morse_code():
    MORSE = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
    FLAG = "picoCTF{"

    file = open("morse_chal.wav", "rb").read()
    file = file.split(b"\x00"*60000)
    for word in file:
        word = word.split(b"\x00"*30000)
        for letter in word:
            letter = letter.split(b"\x00"*6000)
            coded = ''
            for beep in letter:
                if 5000 < len(beep) < 18000:
                    coded += '.'
                elif len(beep) > 23000:
                    coded += "-"        
            letter = list(MORSE.keys())[list(MORSE
                .values()).index(coded)]
            FLAG += letter
        FLAG += "_"
   
    FLAG = FLAG[:-1] + "}"

    print("Flag:", FLAG)

def rail_fence():
    MESSAGE = "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA"
    LEN = len(MESSAGE)
    RAILS = 4
    BLOCKSIZE = 2 * RAILS - 2
    BLOCKS = LEN // BLOCKSIZE
    EXTRA = BLOCKS % RAILS

    rail_cipher = [BLOCKS] * RAILS
    rail_cipher[0] = rail_cipher[-1] = BLOCKS

    if EXTRA >= RAILS:
        rail_cipher[-1] += 1
    elif EXTRA >= 1:
        rail_cipher[0] += 1

    for i in range(1, RAILS - 1):
        rail_cipher[i] = 2 * BLOCKS
        if BLOCKSIZE - 1 <= EXTRA:
            rail_cipher[i] += 2
        elif i <= EXTRA:
            rail_cipher[i] += 1

    position = 0
    for c, i in enumerate(rail_cipher):
        rail_cipher[c] = MESSAGE[position:position + i]
        position += i
    
    FLAG = ""
    c1 = 0
    c2 = 0
    for i in range(BLOCKS + 1):
        try: 
            FLAG += rail_cipher[0][c1]
            for j in rail_cipher[1:-1]:
                FLAG += j[c2]
            FLAG += rail_cipher[-1][c1]
            c2 += 1
            rail_cipher.reverse()
            for j in rail_cipher[1:-1]:
                FLAG += j[c2]
            rail_cipher.reverse()
            c1 += 1
            c2 += 1
        except:
            break
        
    print(FLAG)

def transposition_trial():
    MESSAGE = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"

    FLAG = ""
    for i in range(0, len(MESSAGE), 3):
        FLAG += MESSAGE[i + 2] + MESSAGE[i:i + 2]

    print(FLAG)

def vigenere():
    import string

    MESSAGE = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
    KEY = "CYLAB" * (len(MESSAGE) // 5 + 1)
    FLAG = ""
    c = 0
    for i in MESSAGE:
        if i in string.digits + "{}_":
            FLAG += i
        else:
            if i in string.ascii_lowercase:
                alphabet = string.ascii_lowercase
                KEY = KEY.lower()
            else:
                alphabet = string.ascii_uppercase
                KEY = KEY.upper()
            FLAG += alphabet[(alphabet.index(i) - alphabet.index(KEY[c]))]
            c += 1
    print("Flag:", FLAG)

if __name__ == "__main__":
    #basic_mod1()
    #basic_mod2()
    #credstuff()
    #morse_code()
    #rail_fence()
    #transposition_trial()
    vigenere()
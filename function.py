import simpleaudio as sa

code = {'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',}

alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', ' ']

def morse_to_alphanumeric(morse):
    check = True
    for i in morse:
        if i != '.' and i != '-' and i != ' ':
            check = False

    if check:
        def morse_to_char(morse):
            if morse == '.-':
                return 'A'
            if morse == '-...':
                return 'B'
            if morse == '-.-.':
                return 'C'
            if morse == '-..':
                return 'D'
            if morse == '.':
                return 'E'
            if morse == '..-.':
                return 'F'
            if morse == '--.':
                return 'G'
            if morse == '....':
                return 'H'
            if morse == '..':
                return 'I'
            if morse == '.---':
                return 'J'
            if morse == '-.-':
                return 'K'
            if morse == '.-..':
                return 'L'
            if morse == '--':
                return 'M'
            if morse == '-.':
                return 'N'
            if morse == '---':
                return 'O'
            if morse == '.--.':
                return 'P'
            if morse == '--.-':
                return 'Q'
            if morse == '.-.':
                return 'R'
            if morse == '...':
                return 'S'
            if morse == '-':
                return 'T'
            if morse == '..-':
                return 'U'
            if morse == '...-':
                return 'V'
            if morse == '.--':
                return 'W'
            if morse == '-..-':
                return 'X'
            if morse == '-.--':
                return 'Y'
            if morse == '--..':
                return 'Z'

            if morse == '-----':
                return '0'
            if morse == '.----':
                return '1'
            if morse == '..---':
                return '2'
            if morse == '...--':
                return '3'
            if morse == '....-':
                return '4'
            if morse == '.....':
                return '5'
            if morse == '-....':
                return '6'
            if morse == '--...':
                return '7'
            if morse == '---..':
                return '8'
            if morse == '----.':
                return '9'

        k = 0
        message = ''
        while True:
            space = False
            code = ''
            for i in range(len(morse)):
                if k > len(morse) - 1:
                    break

                if morse[k] == ' ':
                    if morse[k + 1] == ' ' and k <= len(morse):
                        k += 1
                        space = True
                    k += 1
                    break
                code += morse[k]
                k += 1

            message += morse_to_char(code)
            if k >= len(morse) - 1:
                break
            if space:
                message += ' '
        return message
    return 'Enter Valid Morse Code'


def alpha_to_morse(message):

    check = True
    for i in message:
        x = False
        for j in alpha_list:
            if i == j:
                x = True
        if not x:
            check = False
            break

    if check:
        morse = ''
        index = 0
        for i in message:
            for j in code:
                if i == j:
                    morse += code[j]
                    break
            morse += ' ' if index < len(message)-1 else ''
            index += 1
        return morse

    return 'Only Alphabets and Numbers are accepted'


dat_sound = sa.WaveObject.from_wave_file("dat.wav")
dit_sound = sa.WaveObject.from_wave_file("dit.wav")
space_sound = sa.WaveObject.from_wave_file("space.wav")

def morse_play(morse):
    for i in morse:
        if i == '-':
            dat_play = dat_sound.play()
            dat_play.wait_done()

        if i == '.':
            dit_play = dit_sound.play()
            dit_play.wait_done()

        if i == ' ':
            space_play = space_sound.play()
            space_play.wait_done()

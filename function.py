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
            global alpha_list, code
            for i in alpha_list:
                if morse == code[i]:
                    return i

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
        for i in range(len(message)):
            if message[i] == 'A':
                morse += '.-'
            if message[i] == 'B':
                morse += '-...'
            if message[i] == 'C':
                morse += '-.-.'
            if message[i] == 'D':
                morse += '-..'
            if message[i] == 'E':
                morse += '.'
            if message[i] == 'F':
                morse += '..-.'
            if message[i] == 'G':
                morse += '--.'
            if message[i] == 'H':
                morse += '....'
            if message[i] == 'I':
                morse += '..'
            if message[i] == 'J':
                morse += '.---'
            if message[i] == 'K':
                morse += '-.-'
            if message[i] == 'L':
                morse += '.-..'
            if message[i] == 'M':
                morse += '--'
            if message[i] == 'N':
                morse += '-.'
            if message[i] == 'O':
                morse += '---'
            if message[i] == 'P':
                morse += '.--.'
            if message[i] == 'Q':
                morse += '--.-'
            if message[i] == 'R':
                morse += '.-.'
            if message[i] == 'S':
                morse += '...'
            if message[i] == 'T':
                morse += '-'
            if message[i] == 'U':
                morse += '..-'
            if message[i] == 'V':
                morse += '...-'
            if message[i] == 'W':
                morse += '.--'
            if message[i] == 'X':
                morse += '-..-'
            if message[i] == 'Y':
                morse += '-.--'
            if message[i] == 'Z':
                morse += '--..'

            if message[i] == '0':
                morse += '-----'
            if message[i] == '1':
                morse += '.----'
            if message[i] == '2':
                morse += '..---'
            if message[i] == '3':
                morse += '...--'
            if message[i] == '4':
                morse += '....-'
            if message[i] == '5':
                morse += '.....'
            if message[i] == '6':
                morse += '-....'
            if message[i] == '7':
                morse += '--...'
            if message[i] == '8':
                morse += '---..'
            if message[i] == '9':
                morse += '----.'
            if i == len(message)-1:
                break
            morse += ' '
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

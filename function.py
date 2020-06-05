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
            global code
            for i in code:
                if code[i]==morse:
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

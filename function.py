import simpleaudio as sa


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
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                  'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                  '9', ' ']
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
            if message[i] == 'a' or message[i] == 'A':
                morse += '.-'
            if message[i] == 'b' or message[i] == 'B':
                morse += '-...'
            if message[i] == 'c' or message[i] == 'C':
                morse += '-.-.'
            if message[i] == 'd' or message[i] == 'D':
                morse += '-..'
            if message[i] == 'e' or message[i] == 'E':
                morse += '.'
            if message[i] == 'f' or message[i] == 'F':
                morse += '..-.'
            if message[i] == 'g' or message[i] == 'G':
                morse += '--.'
            if message[i] == 'h' or message[i] == 'H':
                morse += '....'
            if message[i] == 'i' or message[i] == 'I':
                morse += '..'
            if message[i] == 'j' or message[i] == 'J':
                morse += '.---'
            if message[i] == 'k' or message[i] == 'K':
                morse += '-.-'
            if message[i] == 'l' or message[i] == 'L':
                morse += '.-..'
            if message[i] == 'm' or message[i] == 'M':
                morse += '--'
            if message[i] == 'n' or message[i] == 'N':
                morse += '-.'
            if message[i] == 'o' or message[i] == 'O':
                morse += '---'
            if message[i] == 'p' or message[i] == 'P':
                morse += '.--.'
            if message[i] == 'q' or message[i] == 'Q':
                morse += '--.-'
            if message[i] == 'r' or message[i] == 'R':
                morse += '.-.'
            if message[i] == 's' or message[i] == 'S':
                morse += '...'
            if message[i] == 't' or message[i] == 'T':
                morse += '-'
            if message[i] == 'u' or message[i] == 'U':
                morse += '..-'
            if message[i] == 'v' or message[i] == 'V':
                morse += '...-'
            if message[i] == 'w' or message[i] == 'W':
                morse += '.--'
            if message[i] == 'x' or message[i] == 'X':
                morse += '-..-'
            if message[i] == 'y' or message[i] == 'Y':
                morse += '-.--'
            if message[i] == 'z' or message[i] == 'Z':
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


def morse_play(morse):
    for i in morse:
        if i == '-':
            wave_obj = sa.WaveObject.from_wave_file("dat.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()

        if i == '.':
            wave_obj = sa.WaveObject.from_wave_file("dit.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()

        if i == ' ':
            wave_obj = sa.WaveObject.from_wave_file("space.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()

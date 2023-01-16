from morse import MORSE_CODE_DICT

user_text = input('Enter text to translate: ')
translated = []


def translate(text):
    for char in text:
        if char == ' ':
            translated.append('/')
        else:
            translated.append(MORSE_CODE_DICT.get(char.upper()))
        translated.append(' ')
    return "".join(translated)


print(translate(user_text))

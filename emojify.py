import sys


def emojify(input_text):
    output_text = []

    convert = {
        'happy': '\u1F60',
        'sad': '\uFE0F',
        'confused': '\uF615',
    }

    for word in input_text.split():
        if word in convert.keys():
            output_text.append(convert[word])
        else:
            output_text.append(word)

    print(output_text)
    return ' '.join(output_text)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: emojify <INPUT FILE>")
        exit(1)

    input_file = sys.argv[1]
    with open(input_file) as fp:
        text = fp.read()

    print(emojify(text))

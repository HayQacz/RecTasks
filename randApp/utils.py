import random

def mix_word(word):
    if len(word) < 4:
        return word

    f_letter = word[0]
    l_letter = word[-1]
    m_letters = list(word[1:-1])

    random.shuffle(m_letters)

    return f_letter + "".join(m_letters) + l_letter

def process_text(text):
    lines = []

    for line in text.splitlines():

        words = line. split(' ')

        mixed_words = []
        for word in words:
            mixed_words.append(mix_word(word))

        lines.append(' '.join(mixed_words))

    return '\n'.join(lines)
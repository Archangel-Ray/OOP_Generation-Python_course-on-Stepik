"""
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра
    класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке.
    За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

    cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek

Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке
    и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы,
    если они присутствуют, должны оставаться неизменными:

    print(cipher.encode('Биgeek123'))    # Биljjp123
    print(cipher.decode('Биljjp123'))    # Биgeek123

Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].
"""


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    @staticmethod
    def cipher(text, shift):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_text = ''
        for letter in text:
            upp = letter.isupper()
            if letter.lower() in letters:
                letter = letters[(letters.index(letter.lower()) + shift) % 26]
            new_text += letter.upper() if upp else letter
        return new_text

    def encode(self, text):
        return self.cipher(text, self.shift)

    def decode(self, text):
        return self.cipher(text, -self.shift)


# INPUT DATA:

print("\n# TEST_1:")
cipher = CaesarCipher(10)

print(cipher.encode('Beegeek'))
print(cipher.decode('Gjjljjp'))

print("\n# TEST_2:")
cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))

print("\n# TEST_3:")
cipher = CaesarCipher(10)

words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
         'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
         'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
         'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
         'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
         'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
         'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
         'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
         'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print("\n# TEST_4:")
cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print("\n# TEST_5:")
cipher = CaesarCipher(15)

words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏',
         'size🤥',
         'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print("\n# TEST_6:")
cipher = CaesarCipher(1)
print(cipher.encode('ZzzZzz'))
print(cipher.decode('AaaAaa'))

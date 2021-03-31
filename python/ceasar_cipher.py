command = input("CODE / ENCODE: ")
key = list(input("How key(number): "))
text = list(input("Text to code(cap letter): "))


flag_length = True
key_translation = []

while flag_length:
    for letter in key:
        key_translation += letter
        if len(key_translation) >= len(text):
            flag_length = False
            break

word = list('')
if command == 'CODE':
    for iterator_text in text:
        a = ord(iterator_text)
        for iterator_key_translation in key_translation:
            key_translation.pop(0)
            b = a + int(iterator_key_translation)
            while b > 90:
                b -= 26
            c = chr(b)
            word += c
            break

if command == 'ENCODE':
    for iterator_text in text:
        a = ord(iterator_text)
        for iterator_key_translation in key_translation:
            key_translation.pop(0)
            b = a - int(iterator_key_translation)
            while b > 90:
                b -= 26
            c = chr(b)
            word += c
            break

password = ''
for letter in word:
    password += letter
print(password)

'''
https://www.youtube.com/watch?v=-wikR15AYWY&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=4
prepare the secrete message
'''

message = input('Enter your message : ')
key = int(input('How many character you want to shift (1 - 26) ?  '))

secrete_msg = ''

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code+= key;
        if char.isupper():
            if char_code > ord('Z'):
                char_code += 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code-=26
        secrete_msg+=chr(char_code)
    else:
        secrete_msg+=char
print('Encrypted message is : ',secrete_msg)
key = -key
Org_message = ''
for char in secrete_msg:
    if char.isalpha():
        char_code = ord(char)
        char_code+= key;
        if char.isupper():
            if char_code > ord('Z'):
                char_code+=26
            if char_code < ord('A'):
                char_code+=26
        else:
            if char_code > ord('z'):
                char_code-=26
            if char_code < ord('a'):
                char_code-=26
        Org_message+=chr(char_code)
    else:
        Org_message+=char
print('Decrypted message is : ',Org_message)


string = "⭐️ утро 123 hello 😁"

for char in string:
    print(char, end='\t- ')
    for byte in bytes(char, 'utf-8'):
        print(bin(byte)[2:].zfill(8), end='')
    print()

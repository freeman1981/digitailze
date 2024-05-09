def print_str(string: str) -> None:
    for char in string:
        print(char, end='\t- ')
        for byte in bytes(char, 'utf-8'):
            print(bin(byte)[2:].zfill(8), end='')
        print()


print_str("⭐️ утро 123 hello 😁")

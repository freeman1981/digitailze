def print_str_as_bytes_and_chars(string: str) -> None:
    for char in string:
        print(char, end='\t- ')
        for byte in bytes(char, 'utf-8'):
            print(bin(byte)[2:].zfill(8), end='')
        print()


def bytes_to_str(byte_string: bytes) -> str:
    return byte_string.decode('utf-8')


print(bytes_to_str(
    b"\xd0\xb9"  # й
    b"\xd0\xbe"  # о
    b"\xd0\xb4"  # д
    b"\xd1\x83"  # у
))
print(bytes_to_str(
    b"\xd0\xb8\xcc\x86"  # й
    b"\xd0\xbe"  # о
    b"\xd0\xb4"  # д
    b"\xd1\x83"  # у
))

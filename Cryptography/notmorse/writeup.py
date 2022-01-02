import binascii
f = open("notmorse/notMorse.txt", 'r')
morse = f.read()
morse = morse.replace(".", "1")
morse = morse.replace('-', '0')
binary_int = int(morse, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()
print(ascii_text)

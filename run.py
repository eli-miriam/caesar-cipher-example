from pathlib import Path

INPUT_FILEPATH = 'message.csv'
OUTPUT_FILEPATH = 'decrypted_file.csv'

def print_from(filepath: str):
    print(f"\nContents of {filepath}:")
    print(Path(filepath).read_text())

def sanitise(user_input: str):
    try:
        value = int(user_input)
        if value < 0:
            main()
        else:
            value = value % 26
            return value
    except:
        main()
        

def get_user_input():
    user_input = input('\nPlease enter a non-negative integer as the shift value for decryption:')
    return sanitise(user_input)


def shift_char(char: str, shift_value: int):
    # We do this by converting the character into its ASCII representation 
    # (an ordinal value) and essentially performing pointer arithmetic on it.
    ordinal = ord(char)
    shifted_ordinal = ordinal - shift_value

    # The range of upper-case letters have values between 65 and 90,
    # and the range of lower-case letters between 97 and 122. If the
    # shift caused the new ordinal to lie outside these ranges, move it back
    # by adding 26.
    if ((ordinal >= 65) and (shifted_ordinal < 65)) \
        or ((ordinal >= 97) and (shifted_ordinal < 97)):
        shifted_ordinal += 26
    shifted_char = chr(shifted_ordinal)
    return shifted_char


def decrypt(shift_value: int):
    decrypted_contents = ""
    encrypted_contents = Path(INPUT_FILEPATH).read_text() 
    # The next 3 lines would more Pythonically be written as:
    # `for char in encrypted_contents:`
    # - but the problem spec requests a while loop
    i = 0
    while i < len(encrypted_contents):
        char = encrypted_contents[i]
        if char.isalpha():
            shifted_char = shift_char(char, shift_value)
            decrypted_contents += shifted_char
        else:
            decrypted_contents += char
        i += 1
    return decrypted_contents


def main():
    print_from(INPUT_FILEPATH)
    shift_value = get_user_input()
    Path(OUTPUT_FILEPATH).write_text(decrypt(shift_value))
    print_from(OUTPUT_FILEPATH)

if __name__ == "__main__":
    main()
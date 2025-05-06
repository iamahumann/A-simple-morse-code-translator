
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    ' ': '/'
}

# Reverse dictionary
REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encode_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def decode_from_morse(morse_code):
    return ''.join(REVERSE_DICT.get(code, '') for code in morse_code.split())

# Main loop
while True:
    print("\nMorse Code Translator")
    print("1. Encode Text to Morse")
    print("2. Decode Morse to Text")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        user_text = input("Enter text to encode: ")
        print("Morse Code:", encode_to_morse(user_text))
    elif choice == '2':
        user_morse = input("Enter Morse code (use space between letters and '/' for space): ")
        print("Decoded Text:", decode_from_morse(user_morse))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

def caesar_cipher(text, shift, alphabet):
    result = []
    alphabet_length = len(alphabet)
    
    # Loop through each character in the text
    for char in text:
        # If it's in the alphabet, apply the cipher
        if char.isalpha() and char.lower() in alphabet:
            start_index = alphabet.index(char.lower())  # Find the position of the character
            new_index = (start_index + shift) % alphabet_length  # Shift and wrap around the alphabet
            new_char = alphabet[new_index]

            # Maintain the case (upper or lower)
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        elif char.isalpha():
            # Alphabet provided doesn't contain this character; keep it unchanged
            result.append(char)
        else:
            # If it's not a letter, keep the character unchanged
            result.append(char)
    
    # Join the list of characters to form the output string
    return ''.join(result)

def caesar_cipher_shifts(text, alphabet):
    shifts = {}
    for shift in range(1, len(alphabet) + 1):
        shifts[shift] = caesar_cipher(text, shift, alphabet)
    return shifts

def load_words(file_path):
    # Read the words from the file and store them in a set for fast lookup
    with open(file_path, 'r') as file:
        words = set(line.strip().lower() for line in file.readlines())
    return words

def find_matching_shift(text, words_file, alphabet):
    valid_words = load_words(words_file)
    shifts = caesar_cipher_shifts(text, alphabet)
    
    # Go through each shift and check how many words match
    for shift, shifted_text in shifts.items():
        shifted_words = shifted_text.lower().split()
        matched_words = [word for word in shifted_words if word in valid_words]
        
        # Check if majority of the words in the shifted text are in words.txt
        if len(matched_words) > len(shifted_words) / 2:
            print(f"Shift {shift} has majority matching words with words.txt: {shifted_text}")
            return shifted_text, shift
    
    # If no match is found, return None
    return None, None

def show_all_shifts(shifts):
    print("\nNo valid shift found with a majority match in words.txt. Here are all the shifts:\n")
    for shift, shifted_text in shifts.items():
        print(f"Shift {shift}: {shifted_text}")


def encode_menu():
    text = input("Enter the text to encode: ")
    shift = int(input("Enter the shift value: "))
    alphabet_input = input(
        "Any specific alphabet to use when encoding? (leave blank for default abcdefghijklmnopqrstuvwxyz alphabet): "
    )
    if not alphabet_input:
        alphabet_input = "abcdefghijklmnopqrstuvwxyz"
    encoded = caesar_cipher(text, shift, alphabet_input)
    print(f"Encoded text: {encoded}")


def decode_menu():
    cipher_text = input("Enter the ciphered text: ")
    alphabet_input = input(
        "Any specific alphabet to use when decoding? (leave blank for default abcdefghijklmnopqrstuvwxyz alphabet): "
    )
    if not alphabet_input:
        alphabet_input = "abcdefghijklmnopqrstuvwxyz"

    shifts = caesar_cipher_shifts(cipher_text, alphabet_input)
    words_file = "words.txt"  # The path to your words file
    result, shift_used = find_matching_shift(cipher_text, words_file, alphabet_input)

    if result:
        print(f"\nThe uncease string is found using Shift {shift_used}: {result}")
    else:
        print("\nNo valid shift found with a majority match in words.txt.")
        show_all_shifts(shifts)


def main():
    print("Choose an option:")
    print("1. Encode text using Caesar cipher")
    print("2. Decode Caesar cipher")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        encode_menu()
    elif choice == "2":
        decode_menu()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

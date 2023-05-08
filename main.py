import logo
alphabet = []
message_list = []
def generator_words():
    for i in range(32,123):
        alphabet.append(chr(i))



def cesar(direction:str, message:str,num_of_shifts:int)->str:
    global message_list
    for letter in message:
        if letter in alphabet:
            alphabet_index_letter = alphabet.index(letter)
            if direction =="encode":
                if alphabet_index_letter + num_of_shifts < len(alphabet):
                    message_list.append(alphabet[alphabet_index_letter + num_of_shifts])
            elif direction == "decode":
                alphabet_index_letter = alphabet.index(letter)
                all_indexes = len(alphabet) // 2
                all_indexes += alphabet_index_letter
                if all_indexes - num_of_shifts < len(alphabet):
                    message_list.append(alphabet[alphabet_index_letter - num_of_shifts])
    user_word = "".join(message_list)
    return user_word
print(logo.logo)
def main():
    global alphabet,message_list
    message_list = []

    alphabet = []
    for i in range(2):
        generator_words()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet) // 2:
        print("Not enough letters")
        main()
    message = cesar(direction,text,shift)
    print(f"Your message: {message}")
    user_answer = input("You want to restart? Y or N: ")
    if user_answer == "Y":
        return main()
    elif user_answer == "N":
        print("Bye")
        exit()

if __name__ == "__main__":
    main()
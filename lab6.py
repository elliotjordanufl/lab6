# elliot jordan

def encode(to_encode):
    encoded_password = ""
    i = 0
    while i < 8:
        digit_to_add = int(to_encode[i]) + 3
        if digit_to_add < 10:
            encoded_password += str(digit_to_add)
        else:
            encoded_password += str(digit_to_add-10)
        i += 1
    print("Your password has been encoded and stored!")
    return encoded_password


def decode_password(encoded_password):
    password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)  # shift each digit down by 3 numbers
        password += shifted_digit
    return password


def main():
    encoded_password = ""
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    user_choice = int(input("Please enter an option: "))
    if user_choice == 1:
        to_encode = input("Please enter your password to encode: ")
        encoded_password = encode(to_encode)
       # print(encoded_password)
    elif user_choice == 2:
        if not encoded_password:
            print("Please encode a password first.")
        else:
            print(f"The encoded password is {encoded_password},"
                  f"and the original password is {decode_password(encoded_password)}.")
    elif user_choice == 3:
        quit()


if __name__ == "__main__":
    main()

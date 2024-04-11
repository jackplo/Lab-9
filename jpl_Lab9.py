# Jack Lohse

password = ''


def encode(password):
    password = list(password)
    encoded = [str(int(items) + 3) for items in password]
    encoded = ''.join(encoded)
    return encoded


def decode(password):
    decoded = ''
    for i in password:
        decoded += str(int(i)-3)
    return decoded


def main():
    global password

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        selection = int(input("Please enter an option: "))

        if selection == 1:
            to_encode = str(input("Please enter your password to encode: "))
            password = encode(to_encode)
            print('Your password has been encoded and stored!\n')
        elif selection == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        elif selection == 3:
            break


if __name__ == "__main__":
    main()
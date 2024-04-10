# Jack Lohse

password = ''

def encode(password):
    password = list(password)
    encoded = [str(int(items) + 3) for items in password]
    encoded = ''.join(encoded)
    return encoded


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
            pass
        elif selection == 3:
            break


if __name__ == "__main__":
    main()
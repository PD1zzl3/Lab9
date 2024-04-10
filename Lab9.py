#Peyton LeFleur
def encoder(password):
    encodedPassword = ''
    for i in range(len(password)):
        digit = str((int(password[i]) + 3) % 10)
        encodedPassword += digit
    return encodedPassword

def decoder(encodedPassword):
    decodedPassword = ''
    for i in range(len(encodedPassword)):
        newDigit = str((int(encodedPassword[i]) - 3) % 10)
        decodedPassword += newDigit
    return decodedPassword
def main():
    print('Menu' +
    '\n -------------')

    print(' 1. Encode' +
          '\n 2. Decode' +
          '\n 3.Quit')

    while True:
        print('Please enter an option: ')
        choice = int(input(''))
        if choice == 1:
            password = input('Please enter your passweord to encode: ')
            encodedPassword = encoder(password)
        elif choice == 2:
            decodedPassword = decoder(encodedPassword)
            print('The encoded password is: ' + str(encodedPassword) + ', and the decoded password is ' + str(decodedPassword))
        elif choice == 3:
            return


if __name__ == '__main__':
    main()

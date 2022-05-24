import random
import array


def main():

    while True:
        try:
            length = int(input("Please input the length of a password: "))

            if length <= 4:
                print("The password must be length of 5 or more characters.")
                continue

            break
        except ValueError:
            print("The input is not acceptable. Please try again.")
            continue

    password = passwordGenerator(length)

    print(f"Password:\n{password}")


def passwordGenerator(length):

    # list of digits
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # list of lower-case characters
    lowerCaseCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # list of upper-case characters
    upperCaseCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # list of special characters
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '.', ',', '?']

    # combine all lists to form one array
    combList = digits + lowerCaseCharacters + upperCaseCharacters + symbols

    # randomly select one character from lists
    randDigit = random.choice(digits)
    randLowerCaseChar = random.choice(lowerCaseCharacters)
    randUpperCaseChar = random.choice(upperCaseCharacters)
    randSymbol = random.choice(symbols)

    # combine randomly selected characters to form temporary password
    tempPass = randDigit + randLowerCaseChar + randUpperCaseChar + randSymbol

    # generate password
    for i in range(length - 4):
        tempPass = tempPass + random.choice(combList)

        tempPassList = array.array('u', tempPass)
        random.shuffle(tempPassList)

    # form the password
    password = ''
    for i in tempPassList:
        password = password + i

    return password


if __name__ == "__main__":
    main()

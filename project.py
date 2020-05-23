DASH_POSITION = 5
MIN_LENGTH = 15
MAX_LENGTH = 45

def main():
    print('\nWelcome to the password generator!'
          '\nThis program helps you create a strong password that is easy to memorize.'
          '\nMake sure no one is standing behind your back.')
    print('\nPlease enter a phrase or several words that you will be able to recall easily. '
          '\nA song lyric or a poem line might be a good idea.'
          '\nRecommended size is ' + str(MIN_LENGTH) + '-' + str(MAX_LENGTH) + ' characters (including spaces).'
          '\nPlease note that this program only supports latin characters and spaces.')
    string = input('\nYour input: ')
    if len(string) < MIN_LENGTH:
        string = input('Your phrase is too short. Please enter a longer one: ')
    if len(string) > MAX_LENGTH:
        answer = input('Your password can be quite difficult to type. '
                       'You might want to consider choosing a shorter phrase.'
                       '\nDo you want to continue the program with this phase? y/n \n')
        if answer == "n":
            password = input('Please enter a new phrase: ')
    # turns the string all lowercase
    password = string.lower()
    # capitalizes the first letters of every word
    password = password.title()
    # removes all spaces
    password = password.replace(" ", "")
    # replaces I, O, E with 1, 0, 3 accordingly
    password = replace_ioe(password)
    # inserts a dash after every nth character (n is defined as a constant DASH_POSITION)
    password = insert_dashes(password, DASH_POSITION)
    print("\nYour password is a result of an algorithm that did the following things:"
          "\n1. capitalized the first letters of every word;"
          "\n2. removed all the spaces;"
          "\n3. replaced letters I, O and E with digits that visually resemble them (1, 0 and 3);"
          "\n4. inserted dashes (-) after every " + str(DASH_POSITION) + "th character.")
    print("\nPlease do not share your new password with anyone. Learning it by heart is better than writing it down."
          "\nIf memorizing it is challenging at first, you can write down "
          "the algorithm without potentially exposing the initial phrase."
          "\nTip: if your new password is long enough, you can use different "
          "parts of it on different websites to avoid having the same password everywhere.")
    print("\nYour new password is:")
    print(password)


def replace_ioe(string):
    string = string.replace("i", "1")
    string = string.replace("o", '0')
    string = string.replace("e", '3')
    return string


def insert_dashes(string, index):
    password = '-'.join(string[i:i + DASH_POSITION] for i in range(0, len(string), DASH_POSITION))
    return password


if __name__ == '__main__':
    main()

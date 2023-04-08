# function to show welcome message
def print_welcome_message(author):
    # welcome message to program
    print("=" * 35)
    print(" welcome to renamer ".title().center(35, "="))
    print(f" author: {author} ".title().center(35, "="))
    print(" i`m happy to use my program ".title().center(35, "="))
    print("=" * 35)


# function to show ending message
def print_end_message():
    # print separator
    print("=" * 35)
    print(" end of program ".title().center(35, "="))
    print("=" * 35)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # import os library to treat with operating system
    import os

    # author name
    __author__ = "Ahmed Hassib Khalil"

    # welcome message
    print_welcome_message(__author__)

    # flag to check if user want to use the program again or not
    is_continue = True



    # ask user if he/shw want to use the program again
    want_to_continue = str(
        input("Do yo want to try again? (Y or N): ")).strip().lower()

    # check the answer
    if want_to_continue == 'n' or want_to_continue == 'N':
        print_end_message()
        is_continue = False

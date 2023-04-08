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

    # get the path from user
    dir_path = str(input("\nEnter your path:: ")).strip()

    # change current working directory to the given path
    os.chdir(dir_path)

    # list all files in it
    files_list = os.listdir(dir_path)

    # check if it is empty directory or not
    if len(files_list) != 0:
        """
        # check number of image or video files to calculate the zero fill
        # if len <= 500 then zfill = 3
        # if len <= 1000 then zfill = 4
        # if len <= 10000 then zfill = 5
        # otherwise zfill = 6
        """
        if len(files_list) <= 500:
            zero_fill = 3
        elif len(files_list) <= 1000:
            zero_fill = 4
        elif len(files_list) <= 10000:
            zero_fill = 5
        else:
            zero_fill = 6

        temp = 0
        # loop on all files in the given path
        for i in range(len(files_list)):
            ext = files_list[i].split(".")[-1].lower()  # get file extension
            # # check if the extension in media types list or not to rename file
            # if ext.lower() in media_types:
            temp += 1  # backup of i
            # prepare the file number
            num = str(temp).zfill(zero_fill)
            name = f"{ext}_{num}.{ext}"  # set the new name
            # rename the image
            os.rename(files_list[i], name)

    # print number of files in the given path
    print(f"Total number of files: {len(files_list)}\n")

    # ask user if he/shw want to use the program again
    want_to_continue = str(
        input("Do yo want to try again? (Y or N): ")).strip().lower()

    # check the answer
    if want_to_continue == 'n' or want_to_continue == 'N':
        print_end_message()
        is_continue = False

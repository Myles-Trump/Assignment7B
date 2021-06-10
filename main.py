#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: June 2021
# This program uses a list to determine the average mark of the user


def main():
    # this function uses a list to determine the average mark of the user

    list_1 = []
    list_2 = []
    final_list = []
    contents_1_int = 0
    contents_2_int = 0

    # input & process
    print("Please enter any string for the first list. Enter -1 to end.")

    while contents_1_int != -1:

        contents_1 = input("Enter any string: ")
        try:
            contents_1_int = int(contents_1)

            if contents_1_int != -1:
                list_1.append(contents_1_int)

            else:
                pass

        except Exception:
            list_1.append(contents_1)

        finally:
            pass

    print("Please enter any string for the second list. Enter -1 to end.")

    while contents_2_int != -1:

        contents_2 = input("Enter any string: ")
        try:
            contents_2_int = int(contents_2)

            if contents_2_int != -1:
                list_2.append(contents_2_int)

            else:
                pass

        except Exception:
            list_2.append(contents_2)

        finally:
            pass

    final_list = list_1 + list_2
    print("Your concentrated list is {0}".format(final_list))


if __name__ == "__main__":
    main()

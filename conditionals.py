################################################################################
# TITLE:       How to use Conditional statements in Python
# DESCRIPTION: Uses if/else if/else/and/or to determine if a statement is true
################################################################################


def main():

    i = 5

    # EXAMPLE 1
    if i > 7:               # is i more then 7?
        print("True")
    else:
        print("False")


    # EXAMPLE 2
    if i > 5 and i < 8:     # is i between 6-7?
        print("True")
    elif i > 1 and i < 8:   # is i between 2-7? Yes it is!
        print("True")
    else:                   # if neither of the above are true output False
        print("False")


    # EXAMPLE 3
    if i == 3 or i == 5:
        print(i)




if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()

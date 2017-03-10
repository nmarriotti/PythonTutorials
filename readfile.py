################################################################################
# TITLE:       Reading files in Python
# DESCRIPTION: Open a text file and read the contents of it.
################################################################################


def main():
    # Call the openFile method and pass it Files/file1.txt
    openFile('Files/file1.txt')

def openFile(filename):
    # Create variable and set it to the contents of the file
    fh = open(filename)
    # Output each line in the file
    for line in fh:
        print(line.strip())


if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()

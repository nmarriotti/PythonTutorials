# Formatting strings to include variables

def main():
    x = 1
    name = "John Smith"
    phone = "555-555-5555"

    # Method 1
    print('{}. Name: {} - Phone number: {}'.format(x, name, phone))
    # Method 2
    print('%s. Name: %s - Phone number: %s' % (x, name, phone))


if __name__ == "__main__":
    main()

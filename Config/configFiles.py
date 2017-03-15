# Searching for something in a string

import configparser

def main():

    cfg = configparser.ConfigParser()
    cfg.read('settings.cfg')

    title = cfg['title']['name']
    city = cfg['contact']['city']
    home = cfg['files']['home']

    print(title)
    print(city)
    print(home)






if __name__ == "__main__":
    main()

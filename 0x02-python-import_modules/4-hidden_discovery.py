#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for title in dir(hidden_4):
        if title.startswith('__'):
            continue
        print("{:s}".format(title))

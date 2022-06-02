#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc < 1:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
        for index in range(1, argc + 1):
            print("{:d}: {}".format(index, argv[index]))
    else:
        print("{:d} arguments:".format(argc))
        for string in range(1, argc + 1):
            print("{:d}: {}".format(string, argv[string]))

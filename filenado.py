#!/usr/local/bin/python3

import sys
import os
import re


def sort_dir(dire):
    """
        Given a directory (string), sort all the single_files
        into folders based on their extension
    """
    directory = str(dire)
    if os.path.isdir(directory):
        for single_file in os.listdir(directory):
            if os.path.isdir(single_file):
                continue
            if single_file[0] == '.':
                print('Hidden file: ' + single_file + ' skipping')
                continue
            if single_file == __file__.replace('./', ''):
                continue

            splitted = re.split(r'\.\s*', single_file)
            if len(splitted) == 1:
                print('No single_file extension, skipping ' + single_file)
                continue
            extension = splitted[-1]
            if os.path.isdir(directory + '/' + extension):
                print("apparently " + directory + '/' + extension + ' is a folder!')
                try:
                    print("String to move to " + directory + '/' + extension + '/' + single_file)
                    os.rename(directory + '/' + single_file, directory + '/' + extension + '/' + single_file)
                    print('moved ' + single_file + ' to ' + '.' + extension + '/' + single_file)
                except OSError:
                    print('Failed to move file: ' + single_file + '!')
            else:
                os.mkdir(directory + '/' + extension)
                print("created " + directory + '/' + extension)
                try:
                    os.rename(directory + '/' + single_file, './' + extension + '/' + single_file)
                except OSError:
                    print('Failed to move file: ' + directory + '!')
    elif os.path.isfile(directory):
        print(directory + ' is not a directory!')
    else:
        print(directory + ' does not exist.')


if __name__ == '__main__':
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        sort_dir(arg)

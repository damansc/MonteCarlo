""" loading in the dictionary txt file. """
import sys

def load(file):
    try:
        with open(file, 'r') as file:
            dict_txt = file.read().strip().split('\n')
            dict_txt = [x.lower() for x in dict_txt]
            return dict_txt
    except IOError as e:
        print("{}\nError opening{}. Ending Program".format(e, file))
        sys.exit(1)

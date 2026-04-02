import sys
from stats import word_count
from stats import char_count
from stats import print_list_dict
from stats import sort_on
from stats import dict_to_list_dicts
from stats import print_list_dict

def main():
    #Checking to see if the user provided 2 arguments, if not exit
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = read_string()
    word_count(file_contents)
    new_contents = char_count(file_contents)
    print_list_dict(dict_to_list_dicts(new_contents))


def read_string():
    with open (sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

main()


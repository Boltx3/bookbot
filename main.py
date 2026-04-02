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
#   print_report(file_contents)
    word_count(file_contents)
    new_contents = char_count(file_contents)
    print_list_dict(dict_to_list_dicts(new_contents))


def read_string():
    with open (sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

#def dict_to_list_dicts(dictionary):
#    return [{"key": key, "value": dictionary[key]} for key in dictionary]

#def sort_on(dict):
#    return dict["value"]

#def print_list_dict(list_dict):
#    list_dict.sort(reverse=True, key=sort_on)
#    for d in list_dict:
#        char = d["key"]
#        count = d["value"]
#        if char.isalpha():
#            print(f"The '{char}' character was found '{count}' times")

#def print_report(file_contents):
#    print (f"--- Begin Report of books/frankenstein.txt --")
#    wc = word_count(file_contents)
#    print (f"{wc} words found in the document\n")
#    char_dict = char_count(file_contents)
#    char_dict_list = dict_to_list_dicts(char_dict)
#    print_list_dict(char_dict_list)

 
main()


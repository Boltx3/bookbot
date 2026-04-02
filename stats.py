def word_count(string):
    count = 0
    words = string.split()
    count += len(words)
    print (f"Found {count} total words")

def char_count(string):
    #Function that counts the nubmer of times a character shows up.
    #Stored into a dic
    char_count = {}
    count = 0 
    #Converts any character to a lowercase
    lowercase_string = string.lower()
    count += len(lowercase_string)
    #loop through the string and count chars
    for char in lowercase_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dict_to_list_dicts(dictionary):
    return [{"key": key, "value": dictionary[key]} for key in dictionary]

def sort_on(dict):
    return dict["value"]

def print_list_dict(list_dict):
    list_dict.sort(reverse=True, key=sort_on)
    for d in list_dict:
        char = d["key"]
        count = d["value"]
        if char.isalpha():
            print(f"{char}: {count}")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        word_count(file_contents)
        char_count(file_contents)

def word_count(string):
    count = 0
    words = string.split()
    count += len(words)
    print(count)

def char_count(string):
    #function that counts the number of times a character shows up.
    #Stored into a dic
    char_count = {}
    count = 0
    #converts any character to lowercase
    lowercase_string = string.lower()
    count += len(lowercase_string)
    #Loop through the string and count freq chars
    for char in lowercase_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
 
main()

def main():
        file_contents = read_string()
       # word_count(file_contents)
       # char_count(file_contents)
        print_report(file_contents)

def read_string():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def word_count(string):
    count = 0
    words = string.split()
    count += len(words)
    return count

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

def print_report(file_contents):
    print (f"--- Begin Report of books/frankenstrin.txt --")
    wc = word_count(file_contents)
    print (f"{wc} words found in the document")
 
main()


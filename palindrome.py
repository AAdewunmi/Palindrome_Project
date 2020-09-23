# Check if a word is a palindrome.
def is_palindrome(string):
    return string.casefold() == string[::-1].casefold()


# Check if a sentence is a palindrome.
def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


word = input("Please enter a word or sentence to check: ")
if is_palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not palindrome".format(word))

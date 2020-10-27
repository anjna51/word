word=input(("Enter a word:"))
if(word == word[::-1]):
    print("The word is a palindrome")
else:
    print("Not a palindrome")
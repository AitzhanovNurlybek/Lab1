def palindrome_check(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    return False


insert_str = str(input())

if palindrome_check(insert_str):
    print("Palindrome")
else:
    print("Not a palindrome")

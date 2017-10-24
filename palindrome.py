def is_palindrome(string):
    i = 0
    j = len(string)-1
    while i < j:
        if string[i].lower() != string[j].lower():
            return print("{} is not a palindrome".format(string))
        i += 1
        j -= 1
    return print("{} is a palindrome".format(string))


is_palindrome("nassan")
is_palindrome("nasan")
is_palindrome("Avi")
is_palindrome("Malayalam")
is_palindrome("abbba")

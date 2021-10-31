def ispalindrome(word):
    word2 = ""

    # This list is included so the program can ignore spaces and punctuation when checking if the sentence is a palindrome.
    notincluded = [" ", ".", "?", "!", ",", ";", ":", "–", "-", "[", "]", "{", "}", "(", ")", "\'", "\""]

    for i in word:
        if i not in notincluded:
            word2 += i

    word2 = word2.lower()

    reverseword2 = ""

    for i in range(len(word2)-1,-1,-1):
        reverseword2+=word2[i]

    if word2 == reverseword2:
        print("Is A Palindrome")
        return True
    else:
        print("Not A Palindrome")
        return False

ispalindrome("Oh, who was it I saw? Oh, who?")

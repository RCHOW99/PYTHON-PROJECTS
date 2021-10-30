def ispalindrome(word):
    word2 = ""

    for i in word:
        if i != ' ':
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

ispalindrome("never odd or even")

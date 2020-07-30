'''
Write a function that will except a string
and return True if that string is a palindrome
or return False if that string is not a palindrome

Note: lowercase or uppercase shoud not matter
'''


def palindrome(str):
    abc=''
    str_l = list(str.lower())
    for i in range (len(str_l)-1,-1,-1):
        abc += str_l[i]
    return  str.lower() == abc
print(palindrome('Kobyłamamałybok'))

def find_palindrome(str):
    """
    :param str: any string
    :return:true if str is a palindrome false otherwise
    """
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return find_palindrome(str[1:-1])
    else:
        return False


print find_palindrome("abcdba")
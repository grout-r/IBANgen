from string import ascii_uppercase


def alphanum_to_num(alphanum_string):
    """
    This function transform a alphanumeric string to a fully digits string according to the IBAN method
    :param alphanum_string: an alphanumeric string
    :return: the modified string
    """
    final = ""
    for char in alphanum_string:
        if char in ascii_uppercase:
            final += str(ascii_uppercase.index(char) + 10)
        else:
            final += char
    return final


def purge_bban(bban):
    """
    This function remove undesired characters from a bban
    :param bban: entry bban
    :return: purged bban
    """
    bban = bban.replace("-", "")
    bban = bban.replace("/", "")
    bban = bban.replace("#", "")
    bban = bban.replace(" ", "")
    return bban


def pretty_print_bank_account(account):
    """
    This function pretty print a bank account according to this application format
    :param account: the dictionary representing the account
    """
    print("The selected country is " + account["name"])
    print("The IBAN is " + account["iban"])

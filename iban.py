from tools import alphanum_to_num, purge_bban


def calc_iban_checksum(bban, country_code):
    """
    This function compute the two digit IBAN checksum according the the IBAN algorithm
    More information may be found here : 
    https://fr.wikipedia.org/wiki/International_Bank_Account_Number
    :param bban: The account bban
    :param country_code: The account country code
    :return: The two digit checksum as an integer
    """
    checksum = int(alphanum_to_num(bban) + alphanum_to_num(country_code) + "00")
    checksum = 98 - (checksum % 97)
    return checksum


def gen_iban_from_bban(bban, country_code):
    """
    This function generate an IBAN from a BBAN according to the IBAN algorithm
    :param bban: The account bban
    :param country_code: The account country code
    :return: The full IBAN as a string
    """
    bban = purge_bban(bban)
    checksum = calc_iban_checksum(bban, country_code)
    checksum = str(checksum)
    if len(checksum) < 2:
        checksum = "0" + checksum
    return country_code + checksum + bban

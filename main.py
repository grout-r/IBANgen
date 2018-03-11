from string import ascii_uppercase, digits

# tools


def alphanum_to_num(alphanum):
    final = ""
    for char in alphanum:
        if char in ascii_uppercase:
            final += str(ascii_uppercase.index(char) + 10)
        else:
            final += char
    return final


def purge_bban(bban):
    bban = bban.replace("-", "")
    bban = bban.replace("/", "")
    bban = bban.replace("#", "")
    bban = bban.replace(" ", "")
    return bban

#iban

def calc_iban_checksum(bban, country_code):
    checksum = int(alphanum_to_num(bban) + alphanum_to_num(country_code) + "00")
    checksum = 98 - (checksum % 97)
    return checksum


def gen_iban_from_bban(bban, country_code):
    bban = purge_bban(bban)
    checksum = calc_iban_checksum(bban, country_code)
    checksum = str(checksum)
    if len(checksum) < 2:
        checksum = "0" + checksum
    return country_code + checksum + bban

 # gen bban


def gen_bban():
    with open("bban_descriptor.json") as desc:
        for row in desc:
            print(row)


def main():
    bban = "123456781234567812345789"
    country_code = "AL"

    gen_bban()

    iban = gen_iban_from_bban(bban, country_code)
    print(iban)
    pass

if __name__ == "__main__":
    main()

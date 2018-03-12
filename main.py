from bban import build_bank_account, gen_bban
from iban import gen_iban_from_bban
from tools import pretty_print_bank_account
from sys import exit


def main():
    """
    This program generate an algorithmically valid IBAN according to the JSON resource file.  
    """
    try:
        bank_account = build_bank_account()
    except FileNotFoundError:
        print("Configuration file not found. Aborting.")
        exit(-1)
    else:
        bank_account["bban"] = gen_bban(bank_account["structure"])
        bank_account["iban"] = gen_iban_from_bban(bank_account["bban"], bank_account["code"])
        pretty_print_bank_account(bank_account)


if __name__ == "__main__":
    main()

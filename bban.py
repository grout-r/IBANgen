import json
import random
from string import ascii_uppercase, digits

bban_charset = {"number": digits, "letter": ascii_uppercase, "alphanum": ascii_uppercase + digits}


def build_bank_account():
    """
    This function open the JSON resource who describe internationals bank account and pick one before returning it
    :return: A dictionary representing the bank account format respecting this specification :
    {
    "code" : "XX",
    "name": "NAME",
    "structure":
    [
      {
        "type":"number", OR "type":"letter" OR "type":"alphanum"
        "repeat":XX
      },
      ...
    ]
  }
    """
    with open("bban_descriptor.json") as description:
        data = json.load(description)
    index = random.randint(0, len(data) - 1)
    return data[index]


def gen_bban(structure):
    """
    This function generate a BBAN according to the given structure
    :param structure: 
    A list representing the BBAN format respecting this specification :
    [
      {
        "type":"number", OR "type":"letter" OR "type":"alphanum"
        "repeat":XX
      },
      ...
    ]

    :return: The generated IBAN as a string
    """
    bban = ""
    for entry in structure:
        charset = bban_charset[entry["type"]]
        for i in range(0, entry["repeat"]):
            bban += charset[random.randint(0, len(charset) - 1)]
    return bban

import helper.log
import config
import http.client
import json
import os

from helper.log import logFail

conn = http.client.HTTPSConnection("tft-api.op.gg")


class STATUS_CODE:
    SUCCESS = 200


def getImagesPath():
    raise NotImplementedError


def get(url, needLang=True, version=""):
    sendUrl = ""
    sendUrl += url
    if needLang:
        sendUrl += "?hl=" + config.CONSTANTS_MANAGER.LANG

    if version != "":
        sendUrl += "&version=" + version

    conn.request(
        "GET",
        sendUrl,
        "",
        config.CONSTANTS_MANAGER.HEADERSLIST,
    )

    response = conn.getresponse()

    if response.code != STATUS_CODE.SUCCESS:
        logFail("Fail to load API " + sendUrl + "!")
        return False

    return json.loads(response.read())


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


def example_encrypt_data():
    text = "mrttaqrhknsw ih puggrur"
    custom_key = "happycoding"

    print(f"\nEncrypted text: {text}")
    print(f"Key: {custom_key}")
    decryption = decrypt(text, custom_key)
    print(f"\nDecrypted text: {decryption}\n")

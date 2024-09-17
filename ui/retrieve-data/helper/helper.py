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

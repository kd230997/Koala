import json
import os
from helper import log, helper
from storage import cache

from fetchData.model import VersionResponse
from storage.cache import saveFileImage


class FILE_CACHE:
    VERSION = "version"
    ITEMS = "items"
    CHAMPIONS = "champion"


class API_ENDPOINT:
    GET_VERSION = "/api/v1/meta/current-season?region=VN"
    GET_ITEMS = "/api/v1/meta/items"
    GET_CHAMPIONS = "/api/v1/meta/champions"


def getVersion():
    result = VersionResponse()
    if cache.checkFileCacheExist(FILE_CACHE.VERSION):
        return cache.getFileCache(FILE_CACHE.VERSION)["data"]["version"][0]

    response = helper.get(url=API_ENDPOINT.GET_VERSION, needLang=False)
    cache.cacheResponseInFile(FILE_CACHE.VERSION, response)
    return response["data"]["version"][0]


def getItems(version):
    response = helper.get(url=API_ENDPOINT.GET_ITEMS, version=version)
    cache.cacheResponseInFile(FILE_CACHE.ITEMS, response)
    return response


def getItemsImage():
    version = getVersion()
    index = 1
    dataList = getItems(version)["data"]
    for item in dataList:
        saveFileImage(
            item["imageUrl"], item["apiName"], version=version, desFolder=FILE_CACHE.ITEMS
        )
        print(index, "Completed download " + item["imageUrl"])
        index += 1


def getChampions(version):
    response = helper.get(url=API_ENDPOINT.GET_CHAMPIONS, version=version)
    cache.cacheResponseInFile(FILE_CACHE.CHAMPIONS, response)
    return response


def getChampionsImage():
    version = getVersion()
    index = 1
    dataList = getChampions(version)["data"]
    for item in dataList:
        saveFileImage(
            item["imageUrl"], item["apiName"], version=version, desFolder=FILE_CACHE.CHAMPIONS
        )
        print(index, "Completed download " + item["imageUrl"])
        index += 1

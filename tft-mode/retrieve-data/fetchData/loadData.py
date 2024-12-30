from helper import helper
from storage import cache

from storage.cache import saveFileImage


class FILE_CACHE:
    VERSION = "version"
    ITEMS = "items"
    CHAMPIONS = "champion"


class API_ENDPOINT:
    GET_VERSION = "/api/v1/meta/current-season?region=VN"
    GET_ITEMS = "/api/v1/meta/items"
    GET_CHAMPIONS = "/api/v1/meta/champions"


def getVersion(needCache=True):
    if cache.checkFileCacheExist(FILE_CACHE.VERSION):
        return cache.getFileCache(FILE_CACHE.VERSION)["data"]["version"][0]

    response = helper.get(url=API_ENDPOINT.GET_VERSION, needLang=False)
    if needCache == True:
        cache.cacheResponseInFile(FILE_CACHE.VERSION, response)

    return response["data"]["version"][0]


def getItems():
    version = getVersion()

    response = helper.get(url=API_ENDPOINT.GET_ITEMS, version=version)
    cache.cacheResponseInFile(FILE_CACHE.ITEMS, response)
    return response


def getItemsImage():
    version = getVersion()
    dataList = getItems()["data"]
    for item in dataList:
        saveFileImage(
            item["imageUrl"],
            item["apiName"],
            version=version,
            desFolder=FILE_CACHE.ITEMS,
        )


def getChampions():
    version = getVersion()

    response = helper.get(url=API_ENDPOINT.GET_CHAMPIONS, version=version)

    cache.cacheResponseInFile(FILE_CACHE.CHAMPIONS, response)

    return response


def getChampionsImage():
    version = getVersion()
    dataList = getChampions()["data"]

    for item in dataList:
        saveFileImage(
            item["imageUrl"],
            item["apiName"],
            version=version,
            desFolder=FILE_CACHE.CHAMPIONS,
        )

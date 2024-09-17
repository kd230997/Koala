import helper.log
import config
import http.client
import json
import os
import urllib.request

cachePath = os.path.join("storage", "cache")


def createDirNotExist(directory):
    if os.path.exists(directory) == False:
        os.makedirs(directory)


def cacheResponseInFile(filePath, content):
    savePath = os.path.join(cachePath, filePath + ".json")
    createDirNotExist(os.path.join(cachePath))
    with open(savePath, "w") as f:
        contentFile = json.dumps(content, indent=2)
        f.write(contentFile)


def getFileCache(filePath):
    if checkCacheExist() == False:
        return None
    with open(os.path.join(cachePath, filePath), "r") as f:
        data = json.load(f)
    return data


def checkFileCacheExist(filePath):
    return os.path.exists(os.path.join(cachePath, filePath))


def checkCacheExist():
    return os.path.exists(cachePath)


def saveFileImage(fileUrl: str, fileName: str, desFolder: str, version: str):
    folderImage = os.path.join("storage", "images", version, desFolder)

    if os.path.exists(folderImage) == False:
        os.makedirs(folderImage)
    try:
        with urllib.request.urlopen(fileUrl) as response:
            with open(folderImage + "/" + fileName + ".png", "wb") as f:
                f.write(response.read())
    except:
        print("Error")

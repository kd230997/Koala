import json
import os
import urllib.request

cachePath = os.path.join("storage", "cache")


def createDirNotExist(directory) -> bool:
    if os.path.exists(directory) == False:
        os.makedirs(directory)

    return os.path.exists(directory)


def cacheResponseInFile(filePath, content):
    savePath = os.path.join(cachePath, filePath + ".json")
    createDirNotExist(
        os.path.join(
            cachePath,
        )
    )
    with open(savePath, "w") as f:
        contentFile = json.dumps(content, indent=2)
        f.write(contentFile)


def getFileCache(filePath):
    if checkFileCacheExist(filePath) == False:
        return None
    with open(os.path.join(cachePath, filePath), "r") as f:
        data = json.load(f)
    return data


def checkFileCacheExist(filePath) -> bool:
    return checkFileExist(os.path.join(cachePath, filePath))


def checkFileExist(filePath) -> bool:
    return os.path.exists(filePath)


def saveFileImage(fileUrl: str, fileName: str, desFolder: str, version: str) -> bool:
    folderImage = os.path.join("storage", "images", version, desFolder)

    createDirNotExist(folderImage)
    filePath = os.path.join(folderImage, f"{fileName}.png")
    if checkFileExist(filePath) is not True:
        try:
            with urllib.request.urlopen(fileUrl) as response:
                with open(filePath, "wb") as f:
                    f.write(response.read())
        except:
            print(f"Error cannot load URL: {fileUrl}")
            return False
        print(f"Completed download {fileUrl}")

    else:
        print(f"Already existed file {filePath}!")

    return True

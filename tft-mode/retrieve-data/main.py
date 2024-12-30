import asyncio
from fetchData.loadData import getChampionsImage, getItemsImage, getChampions, getItems
import os


def getAllInfo():
    try:
        original_dir = os.getcwd()
        web_dir = os.path.join(original_dir, "..", "web")
        os.chdir(web_dir)

        getChampions()
        getItems()
        getItemsImage()
        getChampionsImage()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        os.chdir(original_dir)


def main():
    getAllInfo()


if __name__ == "__main__":
    main()

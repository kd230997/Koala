from fetchData.loadData import getChampionsImage, getItemsImage, getChampions, getItems
from config import CONSTANTS_MANAGER
from helper import helper
import os

import cv2
import numpy as np

if __name__ == "__main__":
    # Change to parent directory
    os.chdir("..")
    getChampions()
    getItems()
    getItemsImage()
    getChampionsImage()

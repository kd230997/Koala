from fetchData.loadData import getChampionsImage, getItemsImage
from config import CONSTANTS_MANAGER
from helper import helper

import cv2
import numpy as np

if __name__ == "__main__":
    cv2.namedWindow("Overlay", cv2.WND_PROP_TOPMOST)

    overlay = np.zeros((600, 800, 3), dtype=np.uint8)

    cv2.putText(
        overlay,
        "Hello, world!",
        (100, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
    )

    cv2.imshow("Overlay", overlay)
    while True:
        if cv2.waitKey(1) == ord("q"):
            break
    # getItemsImage()
    # getChampionsImage()

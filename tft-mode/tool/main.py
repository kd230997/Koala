import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

methods = [
    "cv2.TM_CCOEFF",
    "cv2.TM_CCOEFF_NORMED",
    "cv2.TM_CCORR",
    "cv2.TM_CCORR_NORMED",
    "cv2.TM_SQDIFF",
    "cv2.TM_SQDIFF_NORMED",
]


def find_matches(
    find_image, template_image, min_matches=10, ratio_thresh=0.7, showResult=False
):
    sift = cv2.SIFT_create()
    # detect and compute the keypoints and descriptors with SIFT
    kpFindImage, desFindImage = sift.detectAndCompute(find_image, None)
    kpTemplate, desTemplate = sift.detectAndCompute(template_image, None)

    # Check for insufficient keypoints
    if desFindImage is None or desTemplate is None:
        return False

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=100)  # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desFindImage, desTemplate, k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]

    # Count good matches based on ratio test
    good_matches = 0

    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < ratio_thresh * n.distance:
            matchesMask[i] = [1, 0]
            good_matches += 1

    draw_params = dict(
        matchColor=(0, 255, 0),
        singlePointColor=(255, 0, 0),
        matchesMask=matchesMask,
        flags=cv2.DrawMatchesFlags_DEFAULT,
    )

    # cv2.drawMatchesKnn expects a list of lists as matches.
    imgResult = cv2.drawMatchesKnn(
        find_image,
        kpFindImage,
        template_image,
        kpTemplate,
        matches,
        None,
        **draw_params,
    )
    isFound = good_matches >= min_matches
    if isFound or showResult:
        plt.imshow(imgResult)
        plt.show()
    return isFound


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        imgMatLike = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if imgMatLike is not None:
            images.append((filename, imgMatLike))
    return images


def preprocess_image(image):
    # Noise reduction using Gaussian Blur
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Sharpening the image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(denoised_image, -1, kernel)

    return sharpened_image


findImages = load_images_from_folder(os.path.join(os.getcwd(), "images", "items"))

# Apply preprocessing to all images in findImages
preprocessed_images = [(name, preprocess_image(img)) for name, img in findImages]


plt.subplot(121), plt.imshow(findImages[0][1]), plt.title("Original")
plt.subplot(122), plt.imshow(preprocessed_images[0][1]), plt.title("Processed Image")
plt.show()

template = cv2.imread(
    os.path.join(os.getcwd(), "images", "template", "template.png"),
    cv2.IMREAD_GRAYSCALE,
)
preprocess_template = preprocess_image(template)

for imageName, image in preprocessed_images:
    result = find_matches(image, preprocess_template, 5)
    if result:
        print(f"Found {imageName} in template: {'Yes' if result else 'No'}")
        print("\n")


sample = cv2.imread(
    os.path.join(os.getcwd(), "images", "items", "TFT_Item_Bloodthirster.png"),
    cv2.IMREAD_GRAYSCALE,
)

plt.imshow(sample, cmap="gray")
plt.show()
preprocessed_sample = preprocess_image(sample)

result = find_matches(preprocessed_sample, preprocess_template, 10, 0.7, True)

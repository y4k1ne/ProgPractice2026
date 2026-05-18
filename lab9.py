import cv2
import numpy as np

mode = input("Enter mode (blur / sharpen): ").strip().lower()

image = cv2.imread("input-image-of-wood.jpg")

if image is None:
    print("Could not read image")
    exit()

if mode == "blur":
    result = cv2.GaussianBlur(image, (9, 9), 0)
    output_name = "blurred.jpg"

elif mode == "sharpen":
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    result = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    output_name = "sharpened.jpg"

else:
    print("Unknown mode")
    exit()

cv2.imshow("Original", image)
cv2.imshow("Result", result)

cv2.imwrite(output_name, result)

cv2.waitKey()
cv2.destroyAllWindows()





import cv2
import numpy as np

def convolve_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Check the path.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sharpen_kernel = np.array([[0, -1, 0],
                                [-1, 5, -1],
                                [0, -1, 0]])

    blur_kernel = np.ones((5, 5), np.float32) / 25

    edge_kernel = np.array([[-1, -1, -1],
                             [-1, 8, -1],
                             [-1, -1, -1]])

    sharp_image = cv2.filter2D(gray_image, -1, sharpen_kernel)
    blur_image = cv2.filter2D(gray_image, -1, blur_kernel)
    edge_image = cv2.filter2D(gray_image, -1, edge_kernel)

    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Sharp Image", sharp_image)
    cv2.imshow("Blurred Image", blur_image)
    cv2.imshow("Edge Highlighted Image", edge_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = input("Enter the path to the image: ")
convolve_image(image_path)

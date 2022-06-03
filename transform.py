import cv2


def laplacian(image):
    img = cv2.imread('./static/uploads/'+image)

    return(img)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(gray,(3,3),0)
    # laplacian = cv2.Laplacian(img,cv2.CV_64F)
    # cv2.imwrite('./static/laplacian/'+image, img)


def sobel(image):
    sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
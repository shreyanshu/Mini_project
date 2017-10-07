import cv2
import transfom as t

def detect(img_path):
    image = cv2.imread(img_path)
    image = cv2.resize(image, (960, 540))
    # cv2.imshow("detect",image)
    # cv2.waitKey(0)
    orig = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 100, 100)
    cv2.imshow("detect", edged)
    cv2.waitKey(0)
    # print "I am here in loop"
    # show the original image and the ed
    # ge detected image
    _, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        # print peri
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # print len(approx)

        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    # show the contour (outline) of the piece of paper
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 1)
    warped = t.four_point_transform(orig, screenCnt.reshape(4, 2))
    cropped = cv2.resize(warped, (1500,750), interpolation=cv2.INTER_LINEAR)
    # cv2.imshow('', warped)
    # cv2.waitKey(0)
    cv2.imwrite("cropped.png", cropped)
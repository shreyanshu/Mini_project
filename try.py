import cv2

img = cv2.imread('apple2.jpg')
img = cv2.resize(img, (960, 540))  # Resize image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 50, 50)
# cv2.imshow("edged", edged)                            # Show image
# cv2.waitKey(0)

# _, contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
#
# for c in contours:
#     # approximate the contour
#     peri = cv2.arcLength(c, True)
#     print(peri)
#
#     approx = cv2.approxPolyDP(c, 0.002 * peri, True)
#     print(len(approx))
#     if len(approx) == 4:
#         screenCnt = approx
#         break
#
# cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 1)
# cv2.imshow("contours", img)  # Show image
# cv2.waitKey(0)
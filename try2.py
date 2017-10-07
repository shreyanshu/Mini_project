import cv2
img = cv2.imread('apple.jpg')
img = cv2.resize(img, (960, 540))  # Resize image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 0)

_, image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
_, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# edged = cv2.Canny(gray, 50, 50)
# _, contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
cv2.imshow("contours", image)  # Show image
cv2.waitKey(0)
cv2.imshow("contours", gray)
cv2.waitKey(0)

# cv2.imshow("contours", img)  # Show image
our_contours = []
#
for contour in contours:
    [x, y, w, h] = cv2.boundingRect(contour)
    our_contours.append([x, y, w, h])
    # print(our_contours)
our_contours.sort(key=lambda x: x[0])

index = 1
#
for contour in our_contours:
    [x, y, w, h] = contour
    area = w * h

    if area < 1500:
        continue
    # print(area)
    # print(contour)
    # ik = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = img[y:y + h, x: x + w]
    cropped = cv2.resize(cropped, (32, 32), interpolation=cv2.INTER_LINEAR)
#
    row, col = cropped.shape[:2]
    bottom = cropped[row - 2:row, 0:col]
    bordersize = 2
    border = cv2.copyMakeBorder(cropped, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])

    cv2.imwrite(str(index) + ".png",border)
    index = index+1
    cv2.waitKey(0)
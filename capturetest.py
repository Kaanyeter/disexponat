import cv2

vidcap = cv2.VideoCapture(0)

success, frame = vidcap.read()

cv2.imshow("Webcam", frame)
cv2.waitKey()
vidcap.release()
cv2.destroyAllWindows()
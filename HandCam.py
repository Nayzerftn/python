import cv2
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

if not video.isOpened():
    print("La camera n'est pas ouverte.")
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        print("Erreur lors de la lecture de l'image.")
        break

    hands, img = detector.findHands(frame)

    cv2.imshow('Hand Camera', img)

    if cv2.waitKey(1) == ord('e'):
        break

video.release()
cv2.destroyAllWindows()